# Lab 3 Task C

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab3_TaskC.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab3_TaskC.c
 * ENEL712 Embedded Systems Design - Lab Week 3: LCD, USART, ISRs
 * Task C: USART busy-wait echo and command parsing
 *
 * Part 1: Echo machine - read char, return it (busy-wait)
 * Part 2: Parse string; if command (e.g. "0"-"7") blink that LED, else play sad sound
 * Sad sound: 880-740-659 Hz with 120ms delay (Speaker on PB4)
 */

#include <Labboard.h>

#define BAUD 38400UL
#define F_CPU_HZ 8000000UL

static void play_sad_sound(void)
{
    SpeakerOn();
    SpeakerSetFrequency(880);
    DelayMilliSec(120);
    SpeakerSetFrequency(740);
    DelayMilliSec(120);
    SpeakerSetFrequency(659);
    DelayMilliSec(120);
    SpeakerOff();
}

int main(void)
{
    short r;
    unsigned char led_num;

    LEDSInit();
    LEDSSetMask(0x00);
    SpeakerOff();

    USARTInit((unsigned short)BAUD, 8, 0, 1);

    while (1)
    {
        if (USARTReceiveReady())
        {
            r = USARTReadBuffer();
            /* Lower 8 bits are data; upper bits are errors */
            r &= 0x00FF;

            if (r >= '0' && r <= '7')
            {
                /* Command: blink LED 0-7 */
                led_num = (unsigned char)(r - '0');
                LEDSSetMask(1 << led_num);
                DelayMilliSec(200);
                LEDSSetMask(0x00);
                DelayMilliSec(200);
                LEDSSetMask(1 << led_num);
                DelayMilliSec(200);
                LEDSSetMask(0x00);
            }
            else
            {
                /* Not a command: play sad sound */
                play_sad_sound();
            }

            /* Echo the character back */
            USARTWriteBuffer((unsigned short)r);
        }
    }
    return 0;
}
```
