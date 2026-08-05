# Lab 1 Task D

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab1_TaskD.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab1_TaskD.c
 * ENEL712 Embedded Systems Design
 * Task D: 7-Segment Hex Display
 * 
 * Goal: Display the last pressed button index in hexadecimal on dual 7-segment display
 * Hardware: AT90USB1287 Lab Board
 * Push-buttons routed to PORTA when PE1:PE0 = 01
 * 7-segment display controlled via library functions
 */

#include <Labboard.h>

static unsigned char last_button_index = 0;        // Global variable to track last pressed button index

void MyButtonCallback(BUTTON_EVENT e)              // Button callback - library handles debouncing (Buttons.h: BUTTON_EVENT)
{
    switch (e)
    {
        case PB1_PRESS: last_button_index = 0; SEG7WriteHex(0); break;
        case PB2_PRESS: last_button_index = 1; SEG7WriteHex(1); break;
        case PB3_PRESS: last_button_index = 2; SEG7WriteHex(2); break;
        default: break;
    }
}

int main(void)
{
    SEG7Init();                                    // Initialize 7-segment display (Note: Query mentions CSEG7Init(), try CSEG7Init() if this doesn't compile)
    LEDSInit();                                    // Initialize LEDs on PORTC (optional, for visual feedback)
    SelectIO(SEL_BUTTONS);                         // Configure input multiplexer - sets PE1:PE0 = 01 automatically
    BUTTONInit(MyButtonCallback);                  // Initialize button system - library includes built-in debouncing logic
    SEG7WriteHex(0);                               // Initialize display to show 0 using library function
    
    while(1)                                       // Main loop: continuously poll buttons
    {
        BUTTONPoll();                              // Poll buttons - library handles debouncing and calls callback (call regularly)
    }
    
    return 0;
}
```
