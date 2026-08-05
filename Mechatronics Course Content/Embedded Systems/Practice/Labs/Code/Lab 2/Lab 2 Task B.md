# Lab 2 Task B

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab2_TaskB.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab2_TaskB.c
 * ENEL712 Embedded Systems Design - Lab Week 2: PWM ADC
 * Task B: Read POT1 (ADC2/PF2), display 0-99% on dual 7-segment
 *
 * val_0_99 = (raw * 100) / 1023; no LED bar (PORTC shared with 7-seg)
 */

#include <Labboard.h>

#define ADC_CH_POT1  2                             // POT1 on ADC2 (PF2)

int main(void)
{
    unsigned short raw;
    unsigned char val_0_99;

    SEG7Init();
    ADCInit();

    while (1)
    {
        raw = ADCSingleConvert(ADC_CH_POT1);      // 0-1023
        val_0_99 = (unsigned char)((raw * 100UL) / 1023);  // 0-99, round down
        if (val_0_99 > 99) val_0_99 = 99;
        SEG7WriteLeft(val_0_99 / 10);             // Tens digit
        SEG7WriteRight(val_0_99 % 10);            // Ones digit
    }
    return 0;
}
```
