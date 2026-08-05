# LabBoard Library Functions Reference

> [!info] Course material
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Reference Index|Reference index]] · [[Lab Board Knowledge]] · [[Embedded Systems Practice Index|Practice index]]

## Overview
This document summarizes the available library functions from `Labboard.h` for the AT90USB1287 Lab Board.

---

## LED Functions (Leds.h)
**Hardware**: 8 LEDs connected to PORTC (PC0-PC7)
**Note**: LEDs share hardware with 7-segment display - writing to one affects the other.

### Functions:
- **`void LEDSInit(void)`**
  - Initialize the LED system
  - Sets up PORTC for LED output

- **`void LEDSClear(void)`**
  - Turn off all LEDs

- **`void LEDSTurnOn(unsigned char Number)`**
  - Turn on a specific LED
  - Parameter: LED number (0-7)
  - Example: `LEDSTurnOn(3)` turns on LED 3

- **`void LEDSTurnOff(unsigned char Number)`**
  - Turn off a specific LED
  - Parameter: LED number (0-7)
  - Example: `LEDSTurnOff(3)` turns off LED 3

- **`void LEDSSetMask(unsigned char Bitfield)`**
  - Set LEDs based on bitfield
  - Bit 0 = LED 0, Bit 7 = LED 7
  - Example: `LEDSSetMask(0b00001111)` turns on LEDs 0-3, off LEDs 4-7

---

## Button Functions (Buttons.h)
**Hardware**: Push-buttons routed to PORTA when PE1:PE0 = 01
**Note**: There may be a discrepancy between header definition and actual implementation.

- **`void BUTTONInit(void (*pButtonEvent)(BUTTON_EVENT e))`**
  - Initialize button system with callback
  - Callback receives `BUTTON_EVENT` enum: PB1_PRESS, PB1_RELEASE, PB2_PRESS, PB2_RELEASE, PB3_PRESS, PB3_RELEASE

- **`void BUTTONPoll(void)`**
  - Poll buttons (call regularly in main loop)
  - Handles debouncing internally
  - Triggers callbacks on state changes

**Use `BUTTON_EVENT`** (Buttons.h) — the header is authoritative for this board.

---

## Toggle Switch Functions (Toggles.h)
**Hardware**: Toggle switches routed to PORTA when PE1:PE0 = 00

### Functions:
- **`void TOGGLEInit(pfTOGGLEEVENT epf)`**
  - Initialize toggle switch system
  - Parameter: Callback function pointer
  - Callback signature: `void callback(unsigned char ToggleNumber, unsigned char Level)`
  - `ToggleNumber`: 0-7 (PORTA pin)
  - `Level`: 1 = down/pressed, 0 = up/released

- **`unsigned char TOGGLEState(unsigned char Tid)`**
  - Read current state of a toggle switch (no debouncing)
  - Parameter: Toggle ID (0-7)
  - Returns: 1 if depressed, 0 otherwise
  - **Use only for reading initial state**

- **`void TOGGLEPoll(void)`**
  - Poll toggle switches (call regularly in main loop)
  - Handles debouncing and calls callback on state changes

### Constants:
- `NUMBER_TOGGLES`: 8
- `SW_UP`, `SW_DOWN`: Toggle states

---

## 7-Segment Display Functions (7Segment.h)
**Hardware**: Dual 7-segment display (shares PORTC with LEDs)

### Functions:
- **`void SEG7Init(void)`**
  - Initialize 7-segment displays
  - **Note**: Code uses `CSEG7Init()` - may be an alias or different version

- **`void SEG7WriteHex(unsigned char Byte)`**
  - Display a byte value in hexadecimal (00-FF)
  - Shows on both displays (left = high nibble, right = low nibble)
  - Example: `SEG7WriteHex(0x3A)` displays "3A"

- **`void SEG7WriteLeft(unsigned char Code)`**
  - Write hex-encoded number to left display only
  - Parameter: Hex code (0x00-0x0F for 0-F)

- **`void SEG7WriteRight(unsigned char Code)`**
  - Write hex-encoded number to right display only
  - Parameter: Hex code (0x00-0x0F for 0-F)

**Note**: The query document mentions `CSEG7Init()` but header shows `SEG7Init()`. Check which works with your library.

---

## Delay Functions (Delay.h)

### Functions:
- **`void DelayMicroSec(unsigned short Number)`**
  - Delay for specified microseconds
  - Example: `DelayMicroSec(500)` delays 500 microseconds

- **`void DelayMilliSec(unsigned short Number)`**
  - Delay for specified milliseconds
  - Example: `DelayMilliSec(100)` delays 100 milliseconds

---

## I/O Selection Functions (SelectIO.h)
**Alternative to manual PE1:PE0 configuration**

### Functions:
- **`void SelectIO(IOTYPE device)`**
  - Set PORTA/PORTC I/O configuration
  - Parameters:
    - `SEL_BUTTONS`: Select push-buttons
    - `SEL_TOGGLES`: Select toggle switches
    - `SEL_KEYPAD`: Select keypad
    - `SEL_EXTLCD`: Select external LCD
    - Other options available

- **`unsigned char SelectIOGetState(void)`**
  - Get current SelectIO state

- **`void SelectIOSetState(unsigned char State)`**
  - Restore a previously saved SelectIO state

**Usage Example**:
```c
SelectIO(SEL_BUTTONS);  // Instead of manually setting PE1:PE0 = 01
SelectIO(SEL_TOGGLES);  // Instead of manually setting PE1:PE0 = 00
```

---

## Low-Level Button/Toggle Reading (TogglesButtons.h)
**Direct reading without debouncing**

### Functions:
- **`unsigned char ButtonRead(unsigned char ButtonID)`**
  - Read button state directly (no debouncing)
  - Returns: 0 = not pressed, 1 = pressed
  - Button IDs: `PUSH_1`, `PUSH_2`, `PUSH_3`, `TWSB_1` through `TWSB_5`

- **`unsigned char ToggleRead(unsigned char ToggleID)`**
  - Read toggle switch state directly
  - Returns: 1 = high, 0 = low
  - Toggle IDs: `TOGSW_0` through `TOGSW_7`

---

## Task-Specific Recommendations

### Task A - LEDs
- Use: `LEDSInit()`, `LEDSTurnOn()`, `LEDSTurnOff()`, `DelayMilliSec()`

### Task B - Toggle Switches
**Option 1 (Library - Recommended)**:
- Use: `TOGGLEInit()`, `TOGGLEPoll()` with callback
- Or: `SelectIO(SEL_TOGGLES)` + `TOGGLEState()` in loop

**Option 2 (Direct Reading)**:
- Use: `SelectIO(SEL_TOGGLES)` or manual PE1:PE0 = 00
- Read `PINA` directly and use `LEDSSetMask()`

### Task C - Push-Buttons with Debouncing
**Library Approach**:
- Use: `SelectIO(SEL_BUTTONS)` or manual PE1:PE0 = 01
- Use: `BUTTONInit(callback)`, `BUTTONPoll()` in main loop
- Callback receives button_index and button_state

### Task D - 7-Segment Display
- Use: `CSEG7Init()` or `SEG7Init()` (check which works)
- Use: `SEG7WriteHex(value)` to display hex value
- Combine with Task C button detection

---

## Important Notes

1. **Hardware Conflicts**: LEDs and 7-segment display share PORTC. Writing to one affects the other.

2. **Input Multiplexer**: PE1:PE0 controls what's routed to PORTA:
   - `00` → Toggle switches
   - `01` → Push-buttons/encoder

3. **Function Name Discrepancies**: 
   - Headers show `SEG7Init()` but code/query uses `CSEG7Init()`
   - Button callback signature may differ from header
   - Test which functions work with your library version

4. **Debouncing**: Library functions (`BUTTONPoll()`, `TOGGLEPoll()`) handle debouncing automatically.

5. **SelectIO() Alternative**: Use `SelectIO()` instead of manually configuring PE1:PE0 for cleaner code.

---

## Example Code Patterns

### Pattern 1: Button with Callback (use BUTTON_EVENT)
```c
void MyButtonCallback(BUTTON_EVENT e) {
    switch (e) {
        case PB1_PRESS:   LEDSTurnOn(0); break;
        case PB1_RELEASE: LEDSTurnOff(0); break;
        case PB2_PRESS:   LEDSTurnOn(1); break;
        case PB2_RELEASE: LEDSTurnOff(1); break;
        case PB3_PRESS:   LEDSTurnOn(2); break;
        case PB3_RELEASE: LEDSTurnOff(2); break;
        default: break;
    }
}

int main(void) {
    LEDSInit();
    SelectIO(SEL_BUTTONS);
    BUTTONInit(MyButtonCallback);
    while(1) { BUTTONPoll(); }
}
```

### Pattern 2: Toggle Switches with Callback
```c
void MyToggleCallback(unsigned char ToggleNumber, unsigned char Level) {
    if(Level == SW_DOWN) {
        LEDSTurnOn(ToggleNumber);
    } else {
        LEDSTurnOff(ToggleNumber);
    }
}

int main(void) {
    LEDSInit();
    SelectIO(SEL_TOGGLES);
    TOGGLEInit(MyToggleCallback);
    
    while(1) {
        TOGGLEPoll();
    }
}
```

### Pattern 3: Direct Reading (No Debouncing)
```c
int main(void) {
    LEDSInit();
    SelectIO(SEL_TOGGLES);
    DDRA = 0x00;  // PORTA as input
    
    while(1) {
        uint8_t switches = PINA;
        LEDSSetMask(switches);
    }
}
```
