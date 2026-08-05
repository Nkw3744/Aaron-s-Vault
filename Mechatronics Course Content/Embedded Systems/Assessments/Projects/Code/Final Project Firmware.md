# Final Project Firmware

> [!info] Course material
> [[Final Project Overview|Back]] · Source: `final_project_firmware.c` · [[Architectural Design]] · [[Embedded Digital Communications]]

```c
/*
 * ENEL712 Final Project Firmware
 *
 * AT90USB1287 firmware for the condensation-risk / thermal simulator. It
 * combines two responsibilities in a single main():
 *
 *   1. UART command service (baseline opcodes 0x00–0x0D) for the C# GUI,
 *      driven by the USART1 RX ISR + non-ISR command dispatch.
 *
 *   2. Autonomous condensation + thermal background loop driven by a
 *      Timer3 50 ms tick:
 *        - reads ADC1 (RH), ADC2 (Pot1), ADC3 (head temperature) at 1 Hz;
 *        - computes dew point and margin using the linear Magnus estimate
 *          from the lab-board guide §2.2;
 *        - classifies Safe / Marginal / High risk against the
 *          ≥ 3 °C / 0–3 °C / < 0 °C bands;
 *        - drives PC0–PC2 LEDs (steady / 0.5 Hz / 2 Hz) and the PE2 buzzer
 *          on High Risk;
 *        - drives heater PWM from Pot1 with a 40 °C cutoff + recovery
 *          window; fan PWM tracks ~30 °C; lamp mirrors heater duty.
 *
 * UART protocol (USART1, 38400 baud, 8N1):
 *   Start byte: 0x53
 *   Stop  byte: 0xAA
 *
 *   Read command:  [0x53] [INSTR] [0xAA]
 *     MCU reply:   [DATA]          (1 byte)
 *
 *   Write command: [0x53] [INSTR] [LSB] [MSB] [0xAA]
 *     MCU reply:   [INSTR]        (1 byte ACK)
 *
 * Note: while the background loop is running, INSTR_SET_HEATER, INSTR_SET_MOTOR
 * and INSTR_SET_LIGHT writes are accepted but get overwritten on the next
 * 1 Hz update. PC0..PC2 are reserved for the risk LEDs; PC3..PC7 are still
 * GUI-writable via INSTR_SET_PORTC.
 */

#define F_CPU 8000000UL

#include <avr/io.h>
#include <avr/interrupt.h>
#include <Labboard.h>

/* Framing bytes */
#define START_BYTE 0x53
#define STOP_BYTE  0xAA

/* Instruction codes (must match C# GUI) */
#define INSTR_TXCHECK   0x00
#define INSTR_READ_PINA 0x01
#define INSTR_READ_POT1 0x02
#define INSTR_READ_POT2 0x03
#define INSTR_READ_TEMP 0x04
#define INSTR_READ_LIGHT 0x05
#define INSTR_SET_PORTC 0x0A
#define INSTR_SET_HEATER 0x0B
#define INSTR_SET_LIGHT  0x0C
#define INSTR_SET_MOTOR  0x0D
#define INSTR_READ_SIM_MARGIN  0x10
#define INSTR_READ_SIM_STATUS  0x11
#define INSTR_READ_SIM_DEWPT   0x13
#define INSTR_READ_SIM_POWER   0x14
#define INSTR_READ_SIM_FAN     0x15
#define INSTR_READ_ALARM_FLAGS 0x16
#define INSTR_SET_SIM_DEWPT    0xF0
#define INSTR_CLEAR_SIM_DEWPT  0xF1

/* Condensation + thermal background loop (see LabBoard-Laser-Simulator-Guide.md
 * §2.1, §2.2, §2.4). All temperatures in tenths of a degree Celsius.
 * The room air temperature is held at a firmware default until a future opcode
 * is added (see plan §M5 — currently deferred). */
#define T_AMBIENT_TENTH_DEFAULT  200   /* 20.0 °C */
#define OVERTEMP_TENTH           360   /* 36.0 °C heater cutoff */
#define RECOVERY_TENTH           330   /* 33.0 °C re-arm threshold (hysteresis) */
#define FAN_TARGET_HIGH_TENTH    305   /* fan steps up above this */
#define FAN_TARGET_LOW_TENTH     295   /* fan steps down below this */
#define MARGIN_SAFE_TENTH         30   /* ≥ 3.0 °C → Safe (guide §2.2) */
#define MARGIN_MARGINAL_TENTH      0   /* ≥ 0.0 °C → Marginal */
#define RECOVERY_TICKS             5   /* 5 × 1 s slow ticks → ~5 s heater lock-out */
#define TICKS_PER_SECOND          20   /* 1 s = 20 × 50 ms */
#define BLINK_PERIOD_TICKS        40   /* 2 s blink window */
#define HOST_PWM_HOLD_TICKS       30   /* host command hold time (30 × 50 ms = 1.5 s) */
#define HOST_SESSION_TIMEOUT_TICKS 80  /* 80 × 50 ms = 4 s without host commands */
#define MARGIN_BYTE_OFFSET        100  /* wire encoding: byte = margin_tenth + 100 */

/* Alarm flag bits returned by INSTR_READ_ALARM_FLAGS. */
#define ALARM_FLAG_DOOR_FAULT     (1U << 0) /* SW0 && SW1 */
#define ALARM_FLAG_AXIS_ALARM     (1U << 1) /* deferred feature */
#define ALARM_FLAG_OVERTEMP       (1U << 2) /* optional extension bit */

typedef enum
{
    STATUS_SAFE     = 0,
    STATUS_MARGINAL = 1,
    STATUS_HIGH     = 2
} risk_status_t;

typedef enum
{
    RX_WAIT_START = 0,
    RX_READ_INSTR,
    RX_READ_LSB,
    RX_READ_MSB,
    RX_WAIT_STOP
} rx_state_t;

static volatile rx_state_t g_rx_state = RX_WAIT_START;
static volatile uint8_t    g_rx_instr = 0;
static volatile uint8_t    g_rx_lsb   = 0;
static volatile uint8_t    g_rx_msb   = 0;
static volatile uint8_t    g_cmd_ready = 0;

/* Periodic-loop state. Set by Timer3 ISR, consumed in main. */
static volatile uint8_t    g_tick_50ms = 0;

static uint8_t       g_blink_counter  = 0;    /* 0..(BLINK_PERIOD_TICKS-1) */
static uint8_t       g_sec_counter    = 0;    /* 0..(TICKS_PER_SECOND-1)   */
static int16_t       g_ambient_tenth  = T_AMBIENT_TENTH_DEFAULT;
static int16_t       g_surface_tenth  = 0;
static uint8_t       g_rh_pct         = 0;
static uint8_t       g_pot_pct        = 0;
static int16_t       g_dew_tenth      = 0;
static int16_t       g_margin_tenth   = 0;
static risk_status_t g_status         = STATUS_SAFE;
static uint8_t       g_heater_inhibit = 0;
static uint8_t       g_recovery_count = 0;
static uint8_t       g_overtemp_warn  = 0;    /* sticky flag for future GUI poll */
static uint8_t       g_fan_pct        = 0;
static uint8_t       g_portc_image    = 0;    /* shadow so PC0..PC2 vs PC3..PC7 don't fight */
static uint8_t       g_host_motor_hold_ticks  = 0;
static uint8_t       g_host_heater_hold_ticks = 0;
static uint8_t       g_host_lamp_hold_ticks   = 0;
static uint8_t       g_host_session_started    = 0;
static uint8_t       g_host_session_ticks      = 0;
static uint8_t       g_dew_override_valid      = 0;
static int16_t       g_dew_override_tenth      = 0;
static uint8_t       g_axis_alarm_latched      = 0;
static uint8_t       g_laser_on                = 0;
static uint8_t       g_laser_active            = 0;
static uint8_t       g_lamp_led_bits           = 0;
static volatile uint8_t g_tswb_event_pending   = 0;
static volatile uint8_t g_tswb_last_event      = 0;

/* Forward declarations for helpers defined later in this file. */
static uint8_t adc_read_8bit(uint8_t channel);
static void recompute_condensation_from_cached(void);
static void update_lamp_indicator_leds(void);
static void update_lcd_status(void);
static uint8_t heater_interlock_active(void);

static void tswb_event_handler(TSWB_EVENT e)
{
    g_tswb_last_event = (uint8_t)e;
    g_tswb_event_pending = 1U;
}

static uint8_t is_tswb_direction(uint8_t e)
{
    return ((e == (uint8_t)TSWB_LEFT) ||
            (e == (uint8_t)TSWB_RIGHT) ||
            (e == (uint8_t)TSWB_UP) ||
            (e == (uint8_t)TSWB_DOWN)) ? 1U : 0U;
}

static uint8_t heater_interlock_active(void)
{
    uint8_t sw_bits;
    SelectIO(SEL_TOGGLES);
    sw_bits = PINA;
    if ((sw_bits & 0x01U) == 0U) return 1U;  /* laser switch not enabled */
    if ((sw_bits & 0x02U) != 0U) return 1U;  /* door open */
    if (g_axis_alarm_latched != 0U) return 1U; /* track limit alarm */
    return 0U;
}

static uint8_t clamp_u8_from_i16(int16_t value)
{
    if (value < 0)
    {
        return 0U;
    }
    if (value > 255)
    {
        return 255U;
    }
    return (uint8_t)value;
}

static uint8_t encode_margin_byte(int16_t margin_tenth)
{
    int16_t encoded = (int16_t)(margin_tenth + (int16_t)MARGIN_BYTE_OFFSET);
    return clamp_u8_from_i16(encoded);
}

static uint8_t encode_dew_byte(int16_t dew_tenth)
{
    /* byte wire format is dew point in 0.5 C units (dew_tenth / 5). */
    int16_t dew_half_deg = (int16_t)(dew_tenth / 5);
    return clamp_u8_from_i16(dew_half_deg);
}

static uint8_t read_alarm_flags(void)
{
    uint8_t flags = 0U;
    uint8_t sw_bits;

    SelectIO(SEL_TOGGLES);
    sw_bits = PINA;
    if ((sw_bits & 0x03U) == 0x03U)
    {
        flags |= ALARM_FLAG_DOOR_FAULT;
    }
    if (g_overtemp_warn != 0U)
    {
        flags |= ALARM_FLAG_OVERTEMP;
    }
    if (g_axis_alarm_latched != 0U)
    {
        flags |= ALARM_FLAG_AXIS_ALARM;
    }
    return flags;
}

static uint8_t read_baseline_sensor(uint8_t instr)
{
    switch (instr)
    {
        case INSTR_READ_PINA:
            SelectIO(SEL_TOGGLES);
            return PINA;
        case INSTR_READ_POT1:
            return adc_read_8bit(2U);
        case INSTR_READ_POT2:
            return adc_read_8bit(1U);
        case INSTR_READ_TEMP:
            return adc_read_8bit(3U);
        case INSTR_READ_LIGHT:
            return adc_read_8bit(0U);
        default:
            return 0U;
    }
}

static uint8_t read_sim_extension(uint8_t instr)
{
    switch (instr)
    {
        case INSTR_READ_SIM_MARGIN:
            return encode_margin_byte(g_margin_tenth);
        case INSTR_READ_SIM_STATUS:
            return (uint8_t)g_status;
        case INSTR_READ_SIM_DEWPT:
            return encode_dew_byte(g_dew_tenth);
        case INSTR_READ_SIM_POWER:
            return g_pot_pct;
        case INSTR_READ_SIM_FAN:
            return g_fan_pct;
        case INSTR_READ_ALARM_FLAGS:
            return read_alarm_flags();
        default:
            return 0U;
    }
}

static uint8_t write_actuator_command(uint8_t instr, uint16_t word)
{
    switch (instr)
    {
        case INSTR_SET_PORTC:
        {
            uint8_t value = (uint8_t)(word & 0xFFU);
            g_portc_image = (uint8_t)((g_portc_image & 0x07U) | (value & 0xF8U));
            LEDSSetMask(g_portc_image);
            return INSTR_SET_PORTC;
        }
        case INSTR_SET_MOTOR:
            if (word > 399U) { word = 399U; }
            OCR1A = word;
            g_fan_pct = (uint8_t)(((uint32_t)word * 100U) / 399U);
            g_host_motor_hold_ticks = HOST_PWM_HOLD_TICKS;
            g_host_session_started = 1U;
            g_host_session_ticks = HOST_SESSION_TIMEOUT_TICKS;
            return INSTR_SET_MOTOR;
        case INSTR_SET_LIGHT:
            if (heater_interlock_active() != 0U)
            {
                word = 0U;
            }
            if (word > 399U) { word = 399U; }
            OCR1B = word;
            g_host_lamp_hold_ticks = HOST_PWM_HOLD_TICKS;
            g_host_session_started = 1U;
            g_host_session_ticks = HOST_SESSION_TIMEOUT_TICKS;
            return INSTR_SET_LIGHT;
        case INSTR_SET_HEATER:
            if (heater_interlock_active() != 0U)
            {
                word = 0U;
            }
            if (word > 399U) { word = 399U; }
            OCR1C = word;
            g_host_heater_hold_ticks = HOST_PWM_HOLD_TICKS;
            g_host_session_started = 1U;
            g_host_session_ticks = HOST_SESSION_TIMEOUT_TICKS;
            return INSTR_SET_HEATER;
        case INSTR_SET_SIM_DEWPT:
        {
            uint8_t raw = (uint8_t)(word & 0xFFU);
            g_dew_override_tenth = (int16_t)raw * 5;
            g_dew_override_valid = 1U;
            recompute_condensation_from_cached();
            g_host_session_started = 1U;
            g_host_session_ticks = HOST_SESSION_TIMEOUT_TICKS;
            return INSTR_SET_SIM_DEWPT;
        }
        case INSTR_CLEAR_SIM_DEWPT:
            g_dew_override_valid = 0U;
            recompute_condensation_from_cached();
            g_host_session_started = 1U;
            g_host_session_ticks = HOST_SESSION_TIMEOUT_TICKS;
            return INSTR_CLEAR_SIM_DEWPT;
        default:
            return 0U;
    }
}

static uint8_t instruction_requires_word(uint8_t instr)
{
    switch (instr)
    {
        case INSTR_SET_PORTC:
        case INSTR_SET_HEATER:
        case INSTR_SET_LIGHT:
        case INSTR_SET_MOTOR:
        case INSTR_SET_SIM_DEWPT:
        case INSTR_CLEAR_SIM_DEWPT:
            return 1;
        default:
            return 0;
    }
}

static void usart1_init(void)
{
    /* 38400 baud, 8N1 at 8 MHz */
    const uint16_t ubrr = (uint16_t)((F_CPU / (16UL * 38400UL)) - 1UL);

    UBRR1H = (uint8_t)(ubrr >> 8);
    UBRR1L = (uint8_t)(ubrr & 0xFF);

    UCSR1A = 0x00;
    /* Enable RX, TX and RX Complete interrupt */
    UCSR1B = (1U << RXEN1) | (1U << TXEN1) | (1U << RXCIE1);
    /* 8 data bits, no parity, 1 stop bit */
    UCSR1C = (1U << UCSZ11) | (1U << UCSZ10);
}

static void usart1_send_byte(uint8_t value)
{
    while ((UCSR1A & (1U << UDRE1)) == 0U)
    {
        /* wait for transmit buffer empty */
    }
    UDR1 = value;
}

static void timer1_init(void)
{
    /* Fast PWM, TOP = ICR1 = 399 -> 20 kHz at 8 MHz, prescaler 1 */
    ICR1 = 399U;

    /* Clear OC1A/OC1B/OC1C on compare match, Fast PWM mode (WGM13:0 = 14) */
    TCCR1A = (1U << COM1A1) | (1U << COM1B1) | (1U << COM1C1) | (1U << WGM11);
    TCCR1B = (1U << WGM13) | (1U << WGM12) | (1U << CS10); /* prescaler = 1 */

    /* Set PWM outputs as outputs: PB5 (OC1A), PB6 (OC1B), PB7 (OC1C) */
    DDRB |= (1U << DDB5) | (1U << DDB6) | (1U << DDB7);

    /* Start with all PWM outputs off */
    OCR1A = 0U;
    OCR1B = 0U;
    OCR1C = 0U;
}

static uint8_t adc_read_8bit(uint8_t channel)
{
    unsigned short reading10 = ADCSingleConvert(channel); /* 0..1023 */
    return (uint8_t)(reading10 >> 2); /* 8 MSB */
}

/* ---------------------------------------------------------------------------
 * Condensation + thermal background loop
 *
 * Timer3 fires a CTC compare match every 50 ms; the ISR only sets a flag and
 * the heavy lifting (sensor reads, dew-point math, status update, heater /
 * fan PWM) runs in main(). LED blink and buzzer drive update on every 50 ms
 * tick so the 0.5 Hz / 2 Hz patterns line up cleanly.
 *
 * Heavy work runs every 20 ticks (1 Hz) which matches the thermal loop rate
 * called out in the guide. Keeping arithmetic out of the ISR avoids long
 * critical sections and leaves the UART RX ISR free to grab bytes.
 * ------------------------------------------------------------------------- */
static void timer3_init_50ms(void)
{
    /* 8 MHz / 1024 = 7812.5 Hz; OCR3A = 390 → ~50.0 ms period */
    TCCR3A = 0x00;
    TCCR3B = (1U << WGM32) | (1U << CS32) | (1U << CS30); /* CTC, prescale 1024 */
    OCR3A  = 390U;
    TIMSK3 = (1U << OCIE3A);
}

ISR(TIMER3_COMPA_vect)
{
    g_tick_50ms = 1U;
}

static int16_t adc10_to_surface_tenth(uint16_t adc10)
{
    /* LM35-style 50 mV/°C with AVcc = 5 V → tenths °C ≈ adc10 × 49 / 50. */
    if (adc10 > 1023U)
    {
        adc10 = 1023U;
    }
    return (int16_t)(((uint32_t)adc10 * 49U) / 50U);
}

static uint8_t adc10_to_pct(uint16_t adc10)
{
    if (adc10 > 1023U)
    {
        adc10 = 1023U;
    }
    return (uint8_t)(((uint32_t)adc10 * 100U) / 1023U);
}

static risk_status_t classify_margin(int16_t margin_tenth)
{
    if (margin_tenth >= MARGIN_SAFE_TENTH)
    {
        return STATUS_SAFE;
    }
    if (margin_tenth >= MARGIN_MARGINAL_TENTH)
    {
        return STATUS_MARGINAL;
    }
    return STATUS_HIGH;
}

static void recompute_condensation_from_cached(void)
{
    int16_t rh_deficit;
    rh_deficit = (int16_t)100 - (int16_t)g_rh_pct;
    if (rh_deficit < 0)
    {
        rh_deficit = 0;
    }
    g_dew_tenth = (int16_t)(g_ambient_tenth - (int16_t)(rh_deficit * 2));
    if (g_dew_override_valid != 0U)
    {
        g_dew_tenth = g_dew_override_tenth;
    }
    g_margin_tenth = (int16_t)(g_surface_tenth - g_dew_tenth);
    g_status = classify_margin(g_margin_tenth);
}

static void update_lamp_indicator_leds(void)
{
    uint8_t segments;
    if (g_laser_active == 0U)
    {
        g_lamp_led_bits = 0U;
        return;
    }
    segments = (uint8_t)(((uint16_t)g_pot_pct * 5U + 99U) / 100U);
    if (segments > 5U)
    {
        segments = 5U;
    }
    if (segments == 0U)
    {
        g_lamp_led_bits = 0U;
    }
    else
    {
        g_lamp_led_bits = (uint8_t)(((1U << segments) - 1U) << 3);
    }
}

static void lcd_write_line(uint8_t row, const char *text)
{
    unsigned char line[20];
    unsigned char i = 0U;
    while (i < 20U)
    {
        if (text[i] == '\0')
        {
            break;
        }
        line[i] = (unsigned char)text[i];
        i++;
    }
    while (i < 20U)
    {
        line[i] = ' ';
        i++;
    }
    SLCDSetCursorPosition(row, 0U);
    SLCDWriteBuffer(line, 20U);
}

static void update_lcd_status(void)
{
    lcd_write_line(0U, "Laser Safety Status");
    if (g_status == STATUS_SAFE)
    {
        lcd_write_line(1U, "Condensation: SAFE");
    }
    else if (g_status == STATUS_MARGINAL)
    {
        lcd_write_line(1U, "Condensation: CAUTN");
    }
    else
    {
        lcd_write_line(1U, "Condensation: HIGH");
    }
    lcd_write_line(2U, (g_laser_active != 0U) ? "Laser Active: ON" : "Laser Active: OFF");
    if (g_axis_alarm_latched != 0U)
    {
        lcd_write_line(3U, "Track limit: ACTIVE");
    }
    else
    {
        lcd_write_line(3U, "Track limit: clear");
    }
}

static void update_outputs_fast(void)
{
    uint8_t led_low_three = 0U;
    uint8_t buzzer_on     = 0U;

    switch (g_status)
    {
        case STATUS_SAFE:
            /* PC0 steady ON */
            led_low_three = 0x01U;
            break;

        case STATUS_MARGINAL:
            /* PC1 at 0.5 Hz: ON for first half of 2 s window, OFF for second */
            led_low_three = (g_blink_counter < (BLINK_PERIOD_TICKS / 2U))
                                ? 0x02U
                                : 0x00U;
            break;

        case STATUS_HIGH:
        default:
            /* PC2 at 2 Hz: toggle every 5 ticks (250 ms); buzzer steady on */
            led_low_three = (((g_blink_counter / 5U) & 1U) == 0U) ? 0x04U : 0x00U;
            buzzer_on     = 1U;
            break;
    }

    /* Firmware owns PC0..PC2 risk + PC3..PC7 lamp bar indicators. */
    g_portc_image = (uint8_t)((g_lamp_led_bits & 0xF8U) | (led_low_three & 0x07U));
    LEDSSetMask(g_portc_image);

    if (buzzer_on != 0U)
    {
        PORTE |= (1U << 2);
    }
    else
    {
        PORTE &= (uint8_t)~(1U << 2);
    }
}

static void update_thermal_slow(void)
{
    uint16_t adc_pot;
    uint16_t adc_temp;
    uint16_t adc_rh;
    uint16_t heater_pwm;
    uint8_t  host_timed_out;
    uint8_t  sw_bits;
    uint8_t  door_open;
    uint8_t  interlock_block;

    adc_pot  = ADCSingleConvert(2U); /* Pot1 / ADC2 (PF2) */
    adc_temp = ADCSingleConvert(3U); /* Surface / ADC3 (PF3) */
    adc_rh   = ADCSingleConvert(1U); /* RH / ADC1 (PF1) */

    g_pot_pct       = adc10_to_pct(adc_pot);
    g_rh_pct        = adc10_to_pct(adc_rh);
    g_surface_tenth = adc10_to_surface_tenth(adc_temp);

    host_timed_out = ((g_host_session_started != 0U) && (g_host_session_ticks == 0U)) ? 1U : 0U;

    SelectIO(SEL_TOGGLES);
    sw_bits = PINA;
    g_laser_on = (sw_bits & 0x01U) ? 1U : 0U;
    door_open = (sw_bits & 0x02U) ? 1U : 0U;
    interlock_block = ((g_laser_on == 0U) || (door_open != 0U) || (g_axis_alarm_latched != 0U)) ? 1U : 0U;
    g_laser_active = (interlock_block == 0U) ? 1U : 0U;

    recompute_condensation_from_cached();

    /* 40 °C heater cutoff with hysteresis + minimum recovery time.
     * The Timer3 50 ms tick is what samples the surface temperature, so the
     * overtemp event reaches the heater output through the timer interrupt
     * path rather than a busy-wait in main. */
    if (g_surface_tenth > OVERTEMP_TENTH)
    {
        g_heater_inhibit = 1U;
        g_overtemp_warn  = 1U;
        g_recovery_count = RECOVERY_TICKS;
    }
    else if (g_heater_inhibit != 0U)
    {
        if (g_recovery_count > 0U)
        {
            g_recovery_count--;
        }
        if ((g_recovery_count == 0U) && (g_surface_tenth < RECOVERY_TENTH))
        {
            g_heater_inhibit = 0U;
        }
    }

    if (host_timed_out != 0U)
    {
        OCR1A = 0U;
        OCR1C = 0U;
        g_fan_pct = 0U;
    }
    else if ((g_heater_inhibit != 0U) || (interlock_block != 0U))
    {
        OCR1C = 0U;
    }
    else if (g_host_heater_hold_ticks == 0U)
    {
        heater_pwm = (uint16_t)(((uint16_t)g_pot_pct * 399U) / 100U);
        OCR1C = heater_pwm;
    }

    /* Keep lamp steady whenever laser enable is active. */
    OCR1B = (g_laser_active != 0U) ? 399U : 0U;
    update_lamp_indicator_leds();

    /* Main-loop fan tracker around the ~30 °C set-point from §1 of the guide.
     * Step-based control runs every 1 s so it can't oscillate on a single
     * noisy ADC sample; PWM itself stays in hardware. */
    if ((host_timed_out == 0U) && (g_host_motor_hold_ticks == 0U))
    {
        if (g_surface_tenth > FAN_TARGET_HIGH_TENTH)
        {
            if (g_fan_pct <= 95U)
            {
                g_fan_pct = (uint8_t)(g_fan_pct + 5U);
            }
            else
            {
                g_fan_pct = 100U;
            }
        }
        else if (g_surface_tenth < FAN_TARGET_LOW_TENTH)
        {
            if (g_fan_pct >= 5U)
            {
                g_fan_pct = (uint8_t)(g_fan_pct - 5U);
            }
            else
            {
                g_fan_pct = 0U;
            }
        }
        OCR1A = (uint16_t)(((uint16_t)g_fan_pct * 399U) / 100U);
    }
    update_lcd_status();
}

static void service_periodic_tick(void)
{
    TSWBPoll();
    if (g_tswb_event_pending != 0U)
    {
        uint8_t e;
        cli();
        e = g_tswb_last_event;
        g_tswb_event_pending = 0U;
        sei();
        if (e == (uint8_t)TSWB_CENTRE)
        {
            g_axis_alarm_latched = 0U;
        }
        else if (is_tswb_direction(e) != 0U)
        {
            g_axis_alarm_latched = 1U;
        }
    }

    if (g_host_session_ticks > 0U)
    {
        g_host_session_ticks--;
    }
    if (g_host_motor_hold_ticks > 0U)
    {
        g_host_motor_hold_ticks--;
    }
    if (g_host_heater_hold_ticks > 0U)
    {
        g_host_heater_hold_ticks--;
    }
    if (g_host_lamp_hold_ticks > 0U)
    {
        g_host_lamp_hold_ticks--;
    }

    g_blink_counter++;
    if (g_blink_counter >= BLINK_PERIOD_TICKS)
    {
        g_blink_counter = 0U;
    }

    g_sec_counter++;
    if (g_sec_counter >= TICKS_PER_SECOND)
    {
        g_sec_counter = 0U;
        update_thermal_slow();
    }

    update_outputs_fast();
}

ISR(USART1_RX_vect)
{
    uint8_t byte = UDR1;

    switch (g_rx_state)
    {
        case RX_WAIT_START:
            if (byte == START_BYTE)
            {
                g_rx_state = RX_READ_INSTR;
            }
            break;

        case RX_READ_INSTR:
            g_rx_instr = byte;
            if (instruction_requires_word(byte))
            {
                g_rx_state = RX_READ_LSB;
            }
            else
            {
                g_rx_state = RX_WAIT_STOP;
            }
            break;

        case RX_READ_LSB:
            g_rx_lsb = byte;
            g_rx_state = RX_READ_MSB;
            break;

        case RX_READ_MSB:
            g_rx_msb = byte;
            g_rx_state = RX_WAIT_STOP;
            break;

        case RX_WAIT_STOP:
            if (byte == STOP_BYTE)
            {
                g_cmd_ready = 1U;
            }
            /* In any case, reset for next packet */
            g_rx_state = RX_WAIT_START;
            break;

        default:
            g_rx_state = RX_WAIT_START;
            break;
    }
}

static void handle_command(uint8_t instr, uint16_t word)
{
    switch (instr)
    {
        case INSTR_TXCHECK:
            usart1_send_byte(0x0FU);
            break;

        case INSTR_READ_PINA:
        case INSTR_READ_POT1:
        case INSTR_READ_POT2:
        case INSTR_READ_TEMP:
        case INSTR_READ_LIGHT:
            usart1_send_byte(read_baseline_sensor(instr));
            break;

        case INSTR_READ_SIM_MARGIN:
        case INSTR_READ_SIM_STATUS:
        case INSTR_READ_SIM_DEWPT:
        case INSTR_READ_SIM_POWER:
        case INSTR_READ_SIM_FAN:
        case INSTR_READ_ALARM_FLAGS:
            usart1_send_byte(read_sim_extension(instr));
            break;

        case INSTR_SET_PORTC:
        case INSTR_SET_MOTOR:
        case INSTR_SET_LIGHT:
        case INSTR_SET_HEATER:
        case INSTR_SET_SIM_DEWPT:
        case INSTR_CLEAR_SIM_DEWPT:
        {
            uint8_t ack = write_actuator_command(instr, word);
            if (ack != 0U)
            {
                usart1_send_byte(ack);
            }
            break;
        }

        default:
            /* Unknown instruction: ignore, no reply */
            break;
    }
}

int main(void)
{
    /* Labboard initialisation */
    LEDSInit();
    ADCInit();
    SelectIO(SEL_TOGGLES); /* so PINA reads switches */
    TSWBInit(tswb_event_handler);
    SLCDInit();
    SLCDDisplayOn();
    SLCDClearScreen();
    SLCDSetBacklightBrightness(8U);

    /* Buzzer (PE2): drive low until High Risk fires. */
    DDRE  |= (1U << 2);
    PORTE &= (uint8_t)~(1U << 2);

    /* Project-specific peripherals */
    timer1_init();
    timer3_init_50ms();
    usart1_init();
    update_lcd_status();

    sei();

    for (;;)
    {
        if (g_cmd_ready != 0U)
        {
            uint8_t  instr;
            uint8_t  lsb;
            uint8_t  msb;
            uint16_t word;

            cli();
            instr = g_rx_instr;
            lsb   = g_rx_lsb;
            msb   = g_rx_msb;
            g_cmd_ready = 0U;
            sei();

            word = (uint16_t)lsb | ((uint16_t)msb << 8);
            handle_command(instr, word);
        }

        if (g_tick_50ms != 0U)
        {
            cli();
            g_tick_50ms = 0U;
            sei();
            service_periodic_tick();
        }
    }

    /* Unreachable */
    /* return 0; */
}
```
