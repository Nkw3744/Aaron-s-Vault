# Lab 2 Task C

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab2_TaskC.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab2_TaskC.c
 * ENEL712 Embedded Systems Design - Lab Week 2: PWM ADC
 * Task C: Fan PWM 5% steps via TSWB Left (decrease) / Right (increase)
 *
 * fan_pwm 5-100%, clamp after each step; MotorON(), MotorPWM(fan_pwm)
 */

#include <Labboard.h>

static unsigned char fan_pwm = 50;                 // 5-100, start 50%

void TSWBHandler(TSWB_EVENT e)
{
    switch (e)
    {
        case TSWB_LEFT:
            if (fan_pwm > 5)  fan_pwm -= 5;
            break;
        case TSWB_RIGHT:
            if (fan_pwm < 100) fan_pwm += 5;
            break;
        default:
            break;
    }
    MotorPWM(fan_pwm);
}

int main(void)
{
    MotorPWM(fan_pwm);                             // Set duty cycle before enabling motor (match official example order)
    MotorON();
    TSWBInit(TSWBHandler);

    while (1)
    {
        TSWBPoll();
    }
    return 0;
}
```
