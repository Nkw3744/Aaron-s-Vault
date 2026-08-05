# Lab 2 Task A

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab2_TaskA.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab2_TaskA.c
 * ENEL712 Embedded Systems Design - Lab Week 2: PWM ADC
 * Task A: Push buttons (PA0-PA2) play tone while pressed, LED bar shows active button
 *
 * PA0 (PB1) → 200 Hz, PA1 (PB2) → 800 Hz, PA2 (PB3) → 1600 Hz
 * Priority: PB1 > PB2 > PB3 if multiple pressed
 */

#include <Labboard.h>

static unsigned char pressed = 0;                  // Bit 0=PB1, 1=PB2, 2=PB3

static void update_output(void)                    // Apply tone and LED from pressed state; priority PB1 > PB2 > PB3
{
    if (pressed & (1 << 0))                        // PB1 (PA0) highest priority
    {
        LEDSSetMask(0x01);
        SpeakerSetFrequency(200);
        SpeakerOn();
    }
    else if (pressed & (1 << 1))                   // PB2 (PA1)
    {
        LEDSSetMask(0x02);
        SpeakerSetFrequency(800);
        SpeakerOn();
    }
    else if (pressed & (1 << 2))                   // PB3 (PA2)
    {
        LEDSSetMask(0x04);
        SpeakerSetFrequency(1600);
        SpeakerOn();
    }
    else
    {
        LEDSSetMask(0x00);
        SpeakerOff();
    }
}

void ButtonHandler(BUTTON_EVENT e)
{
    switch (e)
    {
        case PB1_PRESS:   pressed |= (1 << 0); break;
        case PB1_RELEASE: pressed &= ~(1 << 0); break;
        case PB2_PRESS:   pressed |= (1 << 1); break;
        case PB2_RELEASE: pressed &= ~(1 << 1); break;
        case PB3_PRESS:   pressed |= (1 << 2); break;
        case PB3_RELEASE: pressed &= ~(1 << 2); break;
        default: break;
    }
    update_output();
}

int main(void)
{
    LEDSInit();
    LEDSSetMask(0x00);
    SpeakerOff();
    SelectIO(SEL_BUTTONS);                         // Route push buttons to PORTA (PA0-PA2)
    BUTTONInit(ButtonHandler);

    while (1)
    {
        BUTTONPoll();
    }
    return 0;
}
```
