# Lab 2 Task D

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab2_TaskD.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab2_TaskD.c
 * ENEL712 Embedded Systems Design - Lab Week 2: PWM ADC
 * Task D: Heater + fan + temperature; two display modes (CENTRE toggles)
 *
 * Mode 0: 7-segment shows temperature (0-99). Mode 1: LED bar shows PWM % (0-8 LEDs).
 * LEFT/RIGHT = fan_pwm, UP/DOWN = heater_pwm. Safety: T>25 fan ON; T>40 heater OFF.
 */

#include <Labboard.h>

static unsigned char fan_pwm = 50;                 // 5-100
static unsigned char heater_pwm = 50;               // 0-100, 0 = off
static unsigned char display_mode = 0;              // 0 = temp on 7-seg, 1 = PWM on LED bar
static unsigned short one_sec_counter = 0;         // ~1 s timer in main loop
static unsigned char last_temp = 0;                 // last temperature for display

void TSWBHandler(TSWB_EVENT e)
{
    switch (e)
    {
        case TSWB_LEFT:
            if (fan_pwm > 5) fan_pwm -= 5;
            MotorPWM(fan_pwm);
            break;
        case TSWB_RIGHT:
            if (fan_pwm < 100) fan_pwm += 5;
            MotorPWM(fan_pwm);
            break;
        case TSWB_DOWN:
            if (heater_pwm > 0) heater_pwm -= 5;
            else heater_pwm = 0;
            if (heater_pwm == 0) HeaterOff();
            else HeaterOn(heater_pwm);
            break;
        case TSWB_UP:
            if (heater_pwm < 100) heater_pwm += 5;
            HeaterOn(heater_pwm);
            break;
        case TSWB_CENTRE:
            display_mode = 1 - display_mode;
            break;
        default:
            break;
    }
}

int main(void)
{
    unsigned short temp_raw;
    unsigned char temp_c;
    unsigned char led_mask;

    ADCInit();                                     // Must be called before Temperature() or any ADC conversion
    HeaterOn(50);
    MotorPWM(fan_pwm);                             // Set duty cycle before enabling motor (match official example order)
    MotorON();
    TSWBInit(TSWBHandler);
    SEG7Init();
    LEDSInit();
    SEG7WriteLeft(0);
    SEG7WriteRight(0);

    while (1)
    {
        TSWBPoll();

        one_sec_counter++;
        if (one_sec_counter >= 1000)                // ~1 s (DelayMilliSec(1) per loop)
        {
            one_sec_counter = 0;
            temp_raw = Temperature();               // ADC3/PF3, 0-1023
            temp_c = (unsigned char)((temp_raw * 99UL) / 1023);  // 0-99 for display
            if (temp_c > 99) temp_c = 99;
            last_temp = temp_c;

            if (temp_raw > 819) HeaterOff();        // Safety: T > 40 °C approx (819/1023*50)
            if (temp_raw > 512) MotorON();          // Safety: T > 25 °C approx; fan ON
            MotorPWM(fan_pwm);
        }

        if (display_mode == 0)                      // Temperature on 7-segment only (no LED bar)
        {
            SEG7WriteLeft(last_temp / 10);         // Tens digit
            SEG7WriteRight(last_temp % 10);       // Ones digit
        }
        else                                        // PWM % on LED bar only (no 7-segment)
        {
            led_mask = (fan_pwm * 8 + 50) / 100;
            if (led_mask > 8) led_mask = 8;
            LEDSSetMask((led_mask >= 8) ? 0xFF : (unsigned char)((1 << led_mask) - 1));
        }

        DelayMilliSec(1);                           // ~1 ms per loop for 1 s counter
    }
    return 0;
}
```
