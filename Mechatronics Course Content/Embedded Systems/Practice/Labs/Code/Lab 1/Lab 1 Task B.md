# Lab 1 Task B

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab1_TaskB.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab1_TaskB.c
 * ENEL712 Embedded Systems Design
 * Task B: Reading Toggle Switches on PORTA
 * 
 * Goal: Read toggle switch states and display them on LEDs
 * Hardware: AT90USB1287 Lab Board
 * Toggle switches routed to PORTA when PE1:PE0 = 00
 * LEDs connected to PORTC (PC0-PC7)
 */

#include <Labboard.h>

static unsigned char toggle_states = 0;           // Global variable to track toggle switch states

void MyToggleCallback(unsigned char ToggleNumber, unsigned char Level)  // Toggle switch callback - called when toggle state changes
{
    if(Level == SW_DOWN)                           // SW_DOWN = 1 (switch depressed)
    {
        toggle_states |= (1 << ToggleNumber);      // Toggle switch down - set corresponding bit
    }
    else                                           // SW_UP = 0 (switch up)
    {
        toggle_states &= ~(1 << ToggleNumber);    // Toggle switch up - clear corresponding bit
    }
    
    LEDSSetMask(toggle_states);                    // Display toggle switch states on LEDs using library function
}

int main(void)
{
    LEDSInit();                                    // Initialize LEDs on PORTC using library function
    SelectIO(SEL_TOGGLES);                         // Configure input multiplexer - sets PE1:PE0 = 00 automatically
    TOGGLEInit(MyToggleCallback);                  // Initialize toggle switch system - library handles debouncing automatically
    
    while(1)                                       // Main loop: continuously poll toggle switches
    {
        TOGGLEPoll();                              // Poll toggle switches - library handles debouncing and calls callback
    }
    
    return 0;
}
```
