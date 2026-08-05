# Lab 1 Task C

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab1_TaskC.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab1_TaskC.c
 * ENEL712 Embedded Systems Design
 * Task C: Push-Buttons with Debouncing
 * 
 * Goal: Handle press/release events from push-buttons with proper debouncing
 * Hardware: AT90USB1287 Lab Board
 * Push-buttons routed to PORTA when PE1:PE0 = 01
 * LEDs connected to PORTC (PC0-PC7)
 */

#include <Labboard.h>

static unsigned char button_states = 0;            // Global variable to track button states for LED display

void MyButtonCallback(BUTTON_EVENT e)              // Button callback - library handles debouncing (Buttons.h: BUTTON_EVENT)
{
    switch (e)
    {
        case PB1_PRESS:   button_states |= (1 << 0); break;
        case PB1_RELEASE: button_states &= ~(1 << 0); break;
        case PB2_PRESS:   button_states |= (1 << 1); break;
        case PB2_RELEASE: button_states &= ~(1 << 1); break;
        case PB3_PRESS:   button_states |= (1 << 2); break;
        case PB3_RELEASE: button_states &= ~(1 << 2); break;
        default: break;
    }
    LEDSSetMask(button_states);                     // Display button states on LEDs
}

int main(void)
{
    LEDSInit();                                    // Initialize LEDs on PORTC using library function
    SelectIO(SEL_BUTTONS);                         // Configure input multiplexer - sets PE1:PE0 = 01 automatically
    BUTTONInit(MyButtonCallback);                  // Initialize button system - library includes built-in debouncing logic
    
    while(1)                                       // Main loop: continuously poll buttons
    {
        BUTTONPoll();                              // Poll buttons - library handles debouncing and calls callback (call regularly)
    }
    
    return 0;
}
```
