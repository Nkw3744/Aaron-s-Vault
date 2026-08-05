# Lab 3 Task B

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab3_TaskB.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab3_TaskB.c
 * ENEL712 Embedded Systems Design - Lab Week 3: LCD, USART, ISRs
 * Task B: LEDs left/right using Timer0 interrupt
 *
 * Goal: Turn LEDs on one at a time, left to right and back, using ISR for delay
 * Timer0 is 8-bit (OCR0A max 255); use ~32ms ticks with counter for ~400ms total
 * Formula: OCR0A = (F_CPU/1024)*(tick_ms/1000) - 1
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <Labboard.h>

#define tick_ms 32UL                               /* ISR period (32ms fits in 8-bit) */
#define TICKS_PER_STEP 13                          /* 13*32ms ≈ 416ms */
#define OCR0A_VAL (((8000000UL/1024UL)*(tick_ms)/1000UL)-1)

static volatile unsigned char led_mask = 0x01;
static volatile signed char direction = 1;
static volatile unsigned char tick_count = 0;

ISR(TIMER0_COMPA_vect)
{
    tick_count++;
    if (tick_count < TICKS_PER_STEP)
        return;
    tick_count = 0;

    LEDSSetMask(led_mask);

    if (direction > 0)
    {
        if (led_mask == 0x80)
        {
            direction = -1;
            led_mask = 0x40;
        }
        else
        {
            led_mask <<= 1;
        }
    }
    else
    {
        if (led_mask == 0x01)
        {
            direction = 1;
            led_mask = 0x02;
        }
        else
        {
            led_mask >>= 1;
        }
    }
}

int main(void)
{
    LEDSInit();
    LEDSSetMask(0x01);

    TCCR0A = (1 << WGM01);                         /* CTC mode */
    TCCR0B = (1 << CS01) | (1 << CS00);            /* Prescaler 1024 */
    OCR0A = (unsigned char)OCR0A_VAL;
    TIMSK0 = (1 << OCIE0A);
    sei();

    while (1)
    {
        /* MCU can sleep - ISR handles LEDs */
    }
    return 0;
}
```
