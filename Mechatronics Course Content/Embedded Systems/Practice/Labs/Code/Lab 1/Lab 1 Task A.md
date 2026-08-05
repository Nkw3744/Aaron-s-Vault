# Lab 1 Task A

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab1_TaskA.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab1_TaskA.c
 * ENEL712 Embedded Systems Design
 * Task A: LEDs on PORTC (Library-based approach)
 * 
 * Goal: Turn LEDs on one at a time sequentially with delays
 * Hardware: AT90USB1287 Lab Board
 * LEDs connected to PORTC (PC0-PC7)
 */

#include <Labboard.h>

int main(void)
{
    LEDSInit();                                    // Initialize LEDs on PORTC using library function
    
    while(1)                                       // Main loop: cycle through LEDs one at a time
    {
        for(unsigned char i = 0; i < 8; i++)      // Turn on each LED one at a time (0-7) with delay
        {
            LEDSTurnOn(i);                         // Library function: Turn on LED at index i
            DelayMilliSec(100);                    // Library function: Wait 100ms
            LEDSTurnOff(i);                        // Library function: Turn off LED at index i
        }
    }
    
    return 0;
}
```
