# Lab Board Knowledge

> [!info] Course material
> [[Embedded Systems Overview|Subject overview]] · [[Embedded Systems Reference Index|Reference index]] · [[Library Functions Reference]] · [[Embedded Systems Practice Index|Practice index]] · [[Lab-Board-IO-Devices.pdf|Board I/O devices PDF]]

**Purpose**: Comprehensive reference for the AT90USB1287 Lab Board (Board 111007) — pin mappings, library functions, hardware details, and implementation notes for all labs.

**Board**: AT90USB1287 Lab Board (Brd111007)  
**Library**: Labboard.h v1.0 (March 2013, D.G.Taylor for AUT University)

---

## ✅ WHAT WE KNOW (Available Information)

### 1. Complete Pin Mapping and Hardware Connections

#### PORTA (PA0-PA7)
- **PA0-PA7**: 8 x Toggle Switches (via multiplexer when PE1:PE0 = 00)
- **PA0-PA7**: 8 x Push Buttons (via multiplexer when PE1:PE0 = 01)
- **PA0-PA3**: Keypad Row 1-3 (when keypad selected)
- **PA4-PA7**: Keypad Col 1-3 (when keypad selected)
- **PA0-PA7**: External Connector (when external connector mode selected)
- **PA3-PA7**: TSWB switches (Up, Right, Down, Enter, Left)

#### PORTB (PB0-PB7)
- **PB0**: Real time clock SPI SS
- **PB1**: Real time clock SPI SCK
- **PB2**: Real time clock SPI MOSI
- **PB3**: Real time clock SPI MISO
- **PB4**: Speaker (OC2A - Timer2 Output Compare A)
- **PB5**: Motor Speed (OC1A/OC0A - Timer1/0 Output Compare A)
- **PB6**: Lamp (OC1B - Timer1 Output Compare B)
- **PB7**: Heater (OC1C/OC0A - Timer1/0 Output Compare)

#### PORTC (PC0-PC7)
- **PC0-PC7**: 8 x LEDs
- **PC0-PC7**: 2 x Hexadecimal 7-Segment Display (shared with LEDs)
- **PC0-PC7**: External Connector (when external connector mode selected)

#### PORTD (PD0-PD7)
- **PD0/PD1**: SCL/SDA - EPROM (I2C address 0x57)
- **PD0/PD1**: SCL/SDA - Multicolour LED (I2C address 0x66)
- **PD0/PD1**: SCL/SDA - LCD (I2C address 0x28)
- **PD2**: UART RX (USB)
- **PD3**: UART TX (USB)
- **PD4**: Frequency input (ICP1 - Input Capture)
- **PD5**: External connector interface selection
- **PD6**: External connector interface selection
- **PD7**: Fan speed (Timer0 clock input)

#### PORTE (PE0-PE7)
- **PE0**: Switches/Buttons/Keypad select for PORTA (multiplexer control)
- **PE1**: Switches/Buttons/Keypad select for PORTA (multiplexer control)
- **PE2**: Buzzer (PIO)
- **PE3**: USB micro
- **PE4**: Real time clock alarm (INT4 - External Interrupt 4)
- **PE5**: Motion sensor PIR (INT5 - External Interrupt 5)
- **PE6**: Rotary encoder Channel B (INT6 - External Interrupt 6)
- **PE7**: Rotary encoder Channel A (INT7 - External Interrupt 7)

#### PORTF (PF0-PF7)
- **PF0**: Light dependent resistor (ADC0)
- **PF1**: Humidity sensor or Variable Resistor 2 (ADC1)
- **PF2**: Microphone or Variable Resistor 1 (ADC2)
- **PF3**: Temperature sensor (ADC3)
- **PF4-PF7**: JTAG

### 2. Complete Library Documentation

#### Library Functions - Comprehensive Details

**LEDs and 7-Segment Display:**
- `LEDSInit()` - Initialize LEDs
- `LEDSClear()` - Turn off all LEDs
- `LEDSTurnOn(unsigned char Number)` - Turn on LED 0-7
- `LEDSTurnOff(unsigned char Number)` - Turn off LED 0-7
- `LEDSSetMask(unsigned char Bitfield)` - Set LEDs via bitmask
- `SEG7Init()` - Initialize 7-segment display
- `SEG7WriteHex(unsigned char Byte)` - Display hex value (00-FF)
- `SEG7WriteLeft(unsigned char Code)` - Write to left display
- `SEG7WriteRight(unsigned char Code)` - Write to right display
- **Note**: LEDs and 7-segment share PORTC - writing to one affects the other

**Buzzer:**
- `Beep()` - Turn on buzzer for 0.5 seconds
- `BuzzerOn()` - Turn on buzzer
- `BuzzerOff()` - Turn off buzzer
- Connected to PE2

**Buttons:**
- `BUTTONInit(void (*pButtonEvent)(BUTTON_EVENT e))` - Initialize with callback
- `BUTTONPoll()` - Poll buttons (removes switch bouncing)
- **Callback receives**: `BUTTON_EVENT` enum (PB1_PRESS, PB1_RELEASE, PB2_PRESS, PB2_RELEASE, PB3_PRESS, PB3_RELEASE)
- **3 push buttons** on PA0-PA2 when `SelectIO(SEL_BUTTONS)` — use `BUTTON_EVENT` (Buttons.h is authoritative)

**Toggle Switches:**
- `TOGGLEInit(pfTOGGLEEVENT epf)` - Initialize with callback
- `TOGGLEPoll()` - Poll switches (removes switch bouncing)
- `TOGGLEState(unsigned char Tid)` - Read current state (no debouncing, for initial state only)
- **Callback receives**: `(unsigned char ToggleNumber, unsigned char Level)`
  - ToggleNumber: 0-7
  - Level: 1 = down/depressed (SW_DOWN), 0 = up (SW_UP) — `TOGGLE_STATE` enum in Toggles.h
- **8 toggle switches** on PA0-PA7 when `SelectIO(SEL_TOGGLES)`

**Keypad:**
- `KEYPADInit(void (*pfKeyEvent)(void *pObj, unsigned char Value), void *pObj)` - Initialize
- `KEYPADSetHandler(...)` - Change callback handler
- `KEYPADPoll()` - Poll keypad (removes switch bouncing)
- **3x4 keypad** (12 keys: 0-9, *, #)
- **Rows**: PA0-PA2, **Columns**: PA4-PA7
- **Callback receives**: ASCII value of key pressed

**TSWB Switches and Rotary Encoder:**
- `TSWBInit(void (*pfTSWBEvent)(TSWB_EVENT e))` - Initialize TSWB switches
- `TSWBPoll()` - Poll TSWB switches
- **TSWB Events**: TSWB_LEFT, TSWB_CENTRE, TSWB_DOWN, TSWB_RIGHT, TSWB_UP
- **Pins**: PA3-PA7 (Up, Right, Down, Enter, Left) — separate from toggle/button/keypad mux; no SelectIO needed
- `REInit(void (*pfIncrement)(signed char Value, unsigned char Direction))` - Initialize rotary encoder
- `REGetCounter()` - Get current counter value (signed short)
- `REGetDirection()` - Get direction (1=clockwise, 0=anticlockwise)
- `REStop()` - Stop encoder callbacks
- **Rotary encoder**: 12 pulses per revolution, non-quadrature encoded
- **Direction detection**: Clockwise = simultaneous rising edges, Anticlockwise = simultaneous falling edges

**7-Segment Display:**
- Displays hexadecimal values (00-FF)
- Shares PORTC with LEDs
- Multiplexed display (dual hex digits)

**LCD Display (4x20 Serial LCD):**
- `SLCDInit()` - Initialize (initiates TWI)
- `SLCDDisplayOn()` / `SLCDDisplayOff()` - Control display
- `SLCDClearScreen()` - Clear screen
- `SLCDHomeCursor()` - Set cursor to position 0,0
- `SLCDSetContrast(unsigned char Value)` - 0-50 (50 = highest contrast)
- `SLCDSetBacklightBrightness(unsigned char Level)` - 1-8 (8 = brightest)
- `SLCDSetCursorPosition(unsigned char Row, unsigned char Column)` - Set cursor (Row 0-3, Col 0-19)
- `SLCDWriteString(char *pBuffer)` - Write string
- `SLCDWriteBuffer(unsigned char *pBuffer, unsigned char NumBytes)` - Write buffer (to display custom char: `unsigned char ch=0; SLCDWriteBuffer(&ch,1);`)
- `SLCDLoadCustomCharacter(unsigned char CharAddress, unsigned char *pBitMap)` - Custom characters (0-7)
- **Custom character format**: 5x8 pixels; 8-byte array, 5 bits per row (MSB unused), row-major top-to-bottom
- **Dimensions**: MAX_ROW=4, MAX_COLUMN=20 (from SLCD4by20.h)
- **Pins**: PD0/PD1 (I2C SCL/SDA)
- I2C address: 0x28

**EPROM:**
- `EPROMInit()` - Initialize TWI interface
- `EPROMWriteByte(unsigned short Address, unsigned char Byte)` - Write single byte (0-0x7FFF)
- `EPROMWritePage(unsigned short Address, unsigned char *pBuffer, unsigned char Number)` - Write page (32 bytes max, page-aligned)
- `EPROMReadByte(unsigned short Address, unsigned char *pByte)` - Read single byte
- `EPROMReadCurrent(unsigned char *pByte)` - Read from current address pointer
- `EPROMReadSequential(unsigned short Address, unsigned char *pBuffer, unsigned short Number)` - Read sequential bytes
- **32K bytes** capacity (0x0000-0x7FFF)
- **32-byte pages** (1024 pages total)
- **I2C address**: 0x57
- **Returns**: 0 for success, TWI error code on failure

**USART:**
- `USARTInit(const unsigned short Baud, const unsigned char DataBits, const unsigned char parity, const unsigned char stopbits)` - Initialize
  - **Baud rates**: 2400, 4800, 9600, 19200, 38400 (max 0.2% error at 8MHz)
  - **Data bits**: 5, 6, 7, 8, 9
  - **Parity**: 0=none, 1=odd, 2=even
  - **Stop bits**: 1 or 2
  - **Returns**: 1=success, -1=invalid baud, -2=invalid data bits, -3=invalid parity, -4=invalid stop bits
- `USARTWriteString(const char *pString)` - Send string
- `USARTWriteBuffer(const unsigned short Data)` - Send byte
- `USARTReadBuffer()` - Read byte (waits for data)
  - **Returns**: Lower bits = data, Upper bits = errors (bit 15=parity, bit 14=overrun, bit 13=frame)
- `USARTReceiveReady()` - Check if data ready (returns 1 if ready, 0 if not)
- `USARTTransmitReady()` - Check if transmitter ready
- **Pins**: PD2=RXD1, PD3=TXD1 (virtual COM port over USB)
- Connected to USB via RS232-to-USB converter (PD2=RX, PD3=TX)

**Motor and Fan Speed:**
- `MotorPWM(unsigned char Percent)` - Set PWM duty cycle (20kHz PWM)
- `MotorON()` - Turn motor on
- `MotorOFF()` - Turn motor off
- `FanSpeedRPM()` - Measure fan speed in RPM
  - **Note**: Short delay in function, doesn't reliably measure very slow speeds
  - **2 pulses per revolution** (2 cutouts in fan casing)
- Motor on PB5 (OC1A/OC0A)
- Fan speed input on PD7 (Timer0 clock input)

**Speaker:**
- `SpeakerOn()` - Turn on speaker (enables OC2A output)
- `SpeakerOff()` - Turn off speaker
- `SpeakerSetFrequency(unsigned short Frequency)` - Set frequency
  - **Range**: 61Hz to 15,625Hz (very approximate)
- Connected to PB4 (OC2A - Timer2 Output Compare A)

**ADC (Analog to Digital Converter):**
- `ADCInit()` - Initialize ADC (must be called first)
- `ADCSingleConvert(unsigned char Ch)` - Single conversion on channel Ch
  - **Returns**: 10-bit value (0-1024 = 0-5V)
  - **Waits** until conversion complete
- `ADCReadingToVolts(unsigned short Reading, char *pOuts)` - Convert to voltage string (7-byte buffer)
- **Reference voltage**: 5V (confirmed)
- **Channels**:
  - **ADC0 (PF0)**: Light level sensor (LDR)
  - **ADC1 (PF1)**: Humidity sensor OR Variable Resistor 2 (selected by toggle switch)
  - **ADC2 (PF2)**: Microphone OR Variable Resistor 1 (selected by toggle switch)
  - **ADC3 (PF3)**: Temperature sensor

**Microphone:**
- `MICInit(void (*pfMicCB)(void))` - Initialize with callback
- `MICPoll()` - Poll microphone system
- `MICFinish()` - Terminate microphone detection
- `MICListen()` - Listen for 5kHz signal over 140 samples (returns cross-correlation value)
- **Threshold**: 25000 (XCOR_THRESHOLD) for detection
- **Callback**: Called when pulse detected (clap/finger snap)
- Connected to PF2 (ADC2)

**Lamp and Light Sensor:**
- `LampOn(unsigned char Percent)` - Turn lamp on with PWM duty cycle
- `LampOff()` - Turn lamp off
- `LightLevel()` - Read light level (returns 0-1024 for 0-5V)
- Lamp on PB6 (OC1B)
- Light sensor on PF0 (ADC0)

**Heater and Temperature:**
- `HeaterOn(unsigned char Percent)` - Turn heater on with PWM duty cycle
- `HeaterOff()` - Turn heater off
- `Temperature()` - Read temperature sensor (returns 0-1024 for 0-5V)
- Heater on PB7 (OC1C/OC0A)
- Temperature sensor on PF3 (ADC3)

**RGB LED:**
- `RGBInit()` - Initialize (initiates TWI)
- `RGBEnable(unsigned char LED_ID)` - Enable LEDs (bitmask: RGB_RED, RGB_GREEN, RGB_BLUE)
- `RGBDisable(unsigned char LedID)` - Disable LEDs
- `RGBWriteRedCurrent(unsigned char MilliAmps)` - Set red current (0-32mA, 0=0.5mA)
- `RGBWriteGreenCurrent(unsigned char MilliAmps)` - Set green current
- `RGBWriteBlueCurrent(unsigned char MilliAmps)` - Set blue current
- `RGBReadRedCurrent(unsigned char *pCurrent)` - Read red current
- `RGBReadGreenCurrent(unsigned char *pCurrent)` - Read green current
- `RGBReadBlueCurrent(unsigned char *pCurrent)` - Read blue current
- **Returns**: 0 for success, TWI error code on failure
- **I2C address**: 0x66
- **Cat3626 RGB LED driver**

**Real Time Clock (RTC):**
- `RTCInit(void (*pfSecondsAlarm)(void))` - Initialize (pass 0 if no seconds callback)
- `RTCSet(pDATETIME pdt)` - Set time/date
- `RTCGet(pDATETIME pdt)` - Get current time/date
- `RTCSecondsAlarm()` - Enable 1-second alarm callback
- `RTCDisableAlarm()` - Disable alarm
- **DATETIME structure**: Seconds, Minutes, Hours (24h), Day (weekday), DayOfMonth, Month, Year (2-digit)
- **SPI interface**: PB0-PB3 (SS, SCK, MOSI, MISO)
- **Alarm interrupt**: PE4 (INT4)
- **Note**: Battery backup RAM available but no battery on lab boards

**Frequency Measurement:**
- `ICPGetFrequency()` - Measure frequency (returns 32-bit value in Hz)
- Uses time difference between positive edges (ICP1 input)
- **Input**: PD4 (ICP1 - Input Capture)
- **Frequency generator**: Selectable frequencies (0-15) via FRSEL button
  - Settings 0-10: Various frequencies (1Hz to 100kHz) at 50% duty
  - Settings 11-15: 1kHz at various duty cycles (10%, 30%, 60%, 80%, 90%)

**PIR Sensor:**
- `PIRRead()` - Read PIR sensor state
  - **Returns**: 1 if active, 0 if not
- Connected to PE5 (INT5)
- No pullup resistor

**Delay Functions:**
- `DelayMilliSec(unsigned short Number)` - Delay in milliseconds
- `DelayMicroSec(unsigned short Number)` - Delay in microseconds

**Interrupts and ISRs (Lab 3):**
- **LabBoard library does NOT provide ISR handlers** - use AVR `ISR()` macro directly
- **AVR libraries required**: `avr/io.h`, `avr/interrupt.h`, `avr/sleep.h`
- **MCU clock**: 8 MHz (F_CPU = 8000000UL) - confirmed for USART, timers
- **sei()** - Enable global interrupts
- **set_sleep_mode(SLEEP_MODE_IDLE)**, **sleep_mode()** - Power-saving idle
- **Random numbers**: AT90USB1287 has no `random()` - use Timer0: `rand_n(n) = TCNT0 % (n+1)`; Timer0 must be running (e.g. `TCCR0B = (1<<CS01)|(1<<CS00)`)

**Timer0 (8-bit) for ISR delays:**
- **Max OCR0A**: 255 (8-bit timer)
- **Formula**: `OCR0A = (F_CPU/1024)*(delay_ms/1000) - 1`; for delays >32ms use software counter in ISR
- **Prescaler 1024**: tick rate = 7812.5 Hz; ~32ms max single period
- **CTC mode**: TCCR0A = (1<<WGM01); compare match triggers TIMER0_COMPA_vect

**USART ISR usage (register-level, no library):**
- **UBRR1**: `UBRR1_VALUE = (F_CPU_HZ/(16UL*BAUD))-1`; UBRR1H = value>>8; UBRR1L = value&0xFF
- **UCSR1C**: 8-bit chars: `(1<<UCSZ11)|(1<<UCSZ10)`
- **UCSR1B**: RXEN1|TXEN1|RXCIE1 (receive interrupt); UDRIE1 for Data Register Empty
- **ISRs**: USART1_RX_vect (read UDR1), USART1_UDRE_vect (write UDR1, disable UDRIE1 when done)

**SelectIO (I/O Multiplexer):**
- `SelectIO(IOTYPE device)` - Set PORTA/PORTC configuration (PE0/PE1 control)
  - `SEL_BUTTONS` - Push buttons (PA0-PA2) to PORTA
  - `SEL_TOGGLES` - Toggle switches (PA0-PA7) to PORTA (note: enum uses SEL_TOGGLES, not SEL_SWITCHES)
  - `SEL_KEYPAD` - Keypad to PORTA
  - `SEL_EXTLCD` - External LCD
  - `SEL_PCOPAI` - PORTC output, PORTA input
  - `SEL_PA0PCI` - PORTA output, PORTC input
  - `SEL_HPAPC` - Half port A, half port C
- `SelectIOGetState()` - Get current SelectIO state
- `SelectIOSetState(unsigned char State)` - Restore saved state
- **Control**: PE0 and PE1 (multiplexer select lines)

### 3. Library Configuration Requirements

**IAR Project Setup:**
- Stack space: **255 bytes** (0xFF)
- Library: **DLIB** (Normal DLIB, not CLIB)
- Include path: Must point to library include folder
- Library file: `LibraryNDB.r90` (No Debug Information version)
- Debugger: Must be set to **Dragon ICE** (not simulator)

**Library Characteristics:**
- Compiled binary library (source not available)
- NDB version = No Debug Information (debugger steps over library functions)
- All header files included via `#include <Labboard.h>`
- Functions organized by module with module prefix (e.g., SLCD, USART, RTC)

### 4. Example Code Patterns

Complete working examples available for:
- LEDs and 7-segment display
- Buzzer
- LCD display (4x20)
- EPROM read/write
- USART communication with printf()
- Toggle switches and buttons
- Keypad
- TSWB switches and rotary encoder
- Motor and fan speed
- Speaker
- ADC and potentiometers
- Microphone
- Lamp and light sensor
- Heater and temperature
- RGB LED
- Real-time clock
- Frequency measurement

### 5. Known Hardware Details

**LED/7-Segment Conflict:**
- LEDs and 7-segment display **share PORTC**
- Writing to LEDs changes 7-segment display and vice versa
- Cannot use both simultaneously - they share the same hardware lines

**ADC Channel Selection:**
- ADC1 and ADC2 have toggle switches on board to select between:
  - ADC1: Humidity sensor OR Variable Resistor 2
  - ADC2: Microphone OR Variable Resistor 1

**Rotary Encoder Details:**
- **Non-quadrature encoded** (signals not 90° out of phase)
- **12 pulses per revolution**
- **Direction detection**:
  - Clockwise: Rising edges simultaneous
  - Anticlockwise: Falling edges simultaneous
- Count increases on rising edge of either signal
- Count decreases on falling edge of either signal

**Fan Speed Measurement:**
- **2 cutouts** in fan casing = 2 pulses per revolution
- Speed measured by counting pulses per second, converted to RPM
- Doesn't reliably measure very slow speeds

**Frequency Generator:**
- Selectable via FRSEL button
- Displayed on 7-segment as FRQ_NUM
- 16 settings (0-15) with various frequencies and duty cycles

**Button Configuration:**
- **3 push buttons** (PB1, PB2, PB3) on PA0-PA2 when buttons selected
- **8 toggle switches** (0-7) on PA0-PA7 when toggles selected
- **5 TSWB switches**: Left, Centre, Down, Right, Up (on PA3-PA7)

**I2C Device Addresses:**
- EPROM: 0x57
- RGB LED: 0x66
- LCD: 0x28

---

## ❌ WHAT IS STILL MISSING (Remaining Gaps)

### 🔴 HIGH PRIORITY - Essential for Development

#### 1. Hardware Schematics
**Status**: Pin mappings known, but circuit details missing

**Missing Information:**
- Complete schematic diagrams
- Hardware multiplexer circuit design
- Pull-up/pull-down resistor values and locations
- Voltage levels (logic high/low thresholds) - though 5V reference confirmed
- Current ratings for outputs
- Power supply requirements and specifications
- Protection circuits

**Impact**: Cannot design custom circuits, troubleshoot hardware issues, or verify electrical safety

#### 2. Timing and Performance Specifications (Detailed)
**Status**: Basic info known, detailed timing missing

**Missing Details:**
- **Debouncing Timing**:
  - Exact sample rate used by `BUTTONPoll()` and `TOGGLEPoll()`
  - Number of consecutive samples required for debounce
  - Exact debounce delay duration
  - Current implementation: Library handles it, but exact algorithm unknown

- **Polling Frequency Requirements**:
  - Minimum `BUTTONPoll()` call frequency (documentation says "regularly")
  - Minimum `TOGGLEPoll()` call frequency
  - Maximum acceptable delay between polls
  - Impact of slow polling on event detection

- **Timer Configurations**:
  - Exact Timer2 settings used by library
  - Prescaler values
  - Interrupt priorities
  - Clock frequency (assumed 8MHz for USART, but not confirmed for all functions)

- **ADC Timing**:
  - Exact conversion time
  - Maximum sampling rate
  - Channel switching delays
  - Settling time requirements

**Impact**: Cannot optimize code, may miss events with slow polling, timing-dependent bugs possible

#### 3. Function Implementation Details (Some Gaps)
**Status**: Most details known, some discrepancies remain

**Missing/Unclear Information:**
- **Button callback**: Use `BUTTON_EVENT` (Buttons.h) — PB1_PRESS, PB1_RELEASE, etc.

- **Error Handling Details**:
  - Complete list of TWI error codes
  - USART error handling details
  - What happens on function failure
  - Recovery procedures

- **Function Limitations**:
  - Maximum parameter values (some known, some not)
  - Edge cases
  - Thread safety (callbacks from ISRs)
  - Reentrancy
  - Memory usage

- **Initialization Order**:
  - Required initialization sequence
  - Dependencies between functions
  - What happens if called out of order

**Impact**: Some uncertainty about correct usage, difficult to debug edge cases

---

### 🟡 MEDIUM PRIORITY - Important for Advanced Usage

#### 4. Hardware Conflicts and Resource Management
**Status**: Some conflicts known, details missing

**Missing Information:**
- **LED/7-Segment Display**:
  - Known: They share PORTC
  - Missing: Exact multiplexing mechanism
  - Missing: Refresh rate requirements for 7-segment
  - Missing: Can they be time-multiplexed?

- **Timer Resource Conflicts**:
  - Which functions use which timers
  - Timer conflicts between functions
  - Priority when conflicts occur
  - Can multiple PWM outputs be used simultaneously?

- **I2C Bus Conflicts**:
  - Multiple I2C devices (EPROM, RGB LED, LCD)
  - Bus arbitration
  - Simultaneous access handling

- **Interrupt Conflicts**:
  - Which functions use interrupts
  - Interrupt priority assignments
  - ISR timing requirements

**Impact**: Resource conflicts, unexpected behavior, may need to avoid certain combinations

#### 5. Communication Interface Details (Advanced)
**Status**: Basic parameters known, advanced features missing

**Missing Information:**
- **USART**:
  - Buffer sizes (transmit/receive)
  - Flow control support
  - Error recovery procedures
  - Clock source details

- **I2C/TWI**:
  - Bus speed (standard/fast/high-speed)
  - Pull-up resistor values
  - Multi-master support
  - Bus timeout handling

- **SPI (RTC)**:
  - Clock speed
  - Mode settings
  - Chip select timing

- **USB**:
  - USB functionality (mentioned as "under development")
  - Device class
  - Configuration details

**Impact**: Advanced communication features unavailable, may have limitations

#### 6. Physical Layout and Mechanical Details
**Status**: Pin mappings known, physical layout unknown

**Missing Information:**
- Board dimensions
- Component locations on board
- Physical labeling
- Connector types and pinouts (external connector)
- Jumper/switch settings (ADC channel selection switches)
- Mounting holes
- Physical button/toggle switch layout

**Impact**: Difficult to identify components, wiring challenges, orientation issues

---

### 🟢 LOW PRIORITY - Nice to Have

#### 7. Register-Level Details
**Status**: Register definitions available, library usage unclear

**Missing Information:**
- Which registers library functions modify
- Register initialization sequences
- Interrupt vector assignments used by library
- Register conflicts with custom code
- Low-level debugging information

**Impact**: Cannot do low-level debugging, may have conflicts with custom register code

#### 8. Version and Compatibility Information
**Status**: Version 1.0 known, other details missing

**Missing Information:**
- Library revision history
- Board revision information
- Compatibility matrix
- Known issues/bugs
- Changelog
- Updates or patches

**Impact**: May encounter unknown bugs, compatibility issues

#### 9. Performance Characteristics
**Status**: Basic info known, detailed performance missing

**Missing Information:**
- Function execution times
- Memory usage per module
- CPU load from library functions
- Power consumption details
- Optimization recommendations

**Impact**: Cannot optimize for performance, power consumption unknown

---

## 📊 UPDATED SUMMARY TABLE

| Category | Status | Priority | Impact if Missing |
|----------|--------|---------|-------------------|
| **Pin Mappings** | ✅ Complete | ✅ Resolved | - |
| **Library Documentation** | ✅ Complete | ✅ Resolved | - |
| **Function Signatures** | ✅ Complete | ✅ Resolved | - |
| **Example Code** | ✅ Complete | ✅ Resolved | - |
| **Hardware Schematics** | ❌ Missing | 🔴 High | Cannot design custom circuits |
| **Detailed Timing Specs** | ⚠️ Partial | 🔴 High | Timing optimization difficult |
| **Function Implementation** | ⚠️ Mostly Known | 🔴 High | Some uncertainty remains |
| **Resource Conflicts** | ⚠️ Partial | 🟡 Medium | May have unexpected conflicts |
| **Communication Details** | ⚠️ Partial | 🟡 Medium | Advanced features unclear |
| **Physical Layout** | ❌ Missing | 🟡 Medium | Component identification difficult |
| **Register Details** | ⚠️ Partial | 🟢 Low | Low-level debugging limited |
| **Version Info** | ⚠️ Partial | 🟢 Low | Compatibility questions |
| **Performance Metrics** | ❌ Missing | 🟢 Low | Optimization difficult |

---

## 🔍 UPDATED RECOMMENDATIONS

### Immediate Actions:
1. **Obtain Hardware Schematics**: 
   - Request schematic diagrams from course materials
   - Document physical layout experimentally
   - Measure electrical characteristics if needed

2. **Timing Analysis**:
   - Test debouncing timing experimentally
   - Measure polling frequency requirements
   - Document timer configurations used

3. **Callback Signatures**: Use `BUTTON_EVENT` for buttons (Buttons.h); `(ToggleNumber, Level)` for toggles (Toggles.h)

### Development Guidelines:
1. **Use Library Functions**: Prefer library functions over direct register access
2. **Follow Examples**: Use provided example code as reference
3. **Test Thoroughly**: Verify behavior experimentally
4. **Check Return Codes**: Always check return values (especially TWI functions)
5. **Initialize Properly**: Call Init functions before using modules
6. **Poll Regularly**: Call Poll functions in main loop regularly

### Known Limitations:
1. **LED/7-Segment Conflict**: Cannot use both simultaneously
2. **Library Source Unavailable**: Cannot debug into library code
3. **NDB Version**: Debugger steps over library functions
4. **8MHz Clock Assumption**: USART functions assume 8MHz clock
5. **Stack Requirement**: Must set stack to 255 bytes
6. **DLIB Required**: Must use DLIB, not CLIB

---

## 📝 NOTES

- **Library Version**: 1.0 (March 2013, D.G.Taylor for AUT University)
- **Board Number**: 111007
- **Processor**: AT90USB1287
- **Development Environment**: IAR Embedded Workbench for AVR
- **Debugger**: Dragon ICE (In Circuit Emulator)
- **Library File**: LibraryNDB.r90 (No Debug Information)
- **USB Interface**: Library still under development (not included)
- **External 20-pin Header**: Not included in library

**ISR Names for AT90USB1287 (Appendix A from Lab 3):**

| ISR Name | Description |
|----------|-------------|
| ADC_vect | ADC Conversion Complete |
| ANALOG_COMP_vect | Analog Comparator |
| EE_READY_vect | EEPROM Ready |
| INT0_vect - INT7_vect | External IRQ 0-7 |
| PCINT0_vect | Pin Change IRQ 0 |
| SPI_STC_vect | SPI Serial Transfer Complete |
| SPM_READY_vect | Store Program Memory Ready |
| TIMER0_COMPA_vect, TIMER0_COMPB_vect, TIMER0_OVF_vect | Timer0 Compare/Overflow |
| TIMER1_CAPT_vect, TIMER1_COMPA/B/C_vect, TIMER1_OVF_vect | Timer1 |
| TIMER2_COMPA_vect, TIMER2_COMPB_vect, TIMER2_OVF_vect | Timer2 |
| TIMER3_CAPT_vect, TIMER3_COMPA/B/C_vect, TIMER3_OVF_vect | Timer3 |
| TWI_vect | Two Wire Serial Interface |
| USART1_RX_vect | USART1 Rx Complete |
| USART1_TX_vect | USART1 Tx Complete |
| USART1_UDRE_vect | USART1 Data Register Empty |
| USB_COM_vect | USB Endpoint/Pipe Interrupt |
| USB_GEN_vect | USB General IRQ |
| WDT_vect | Watchdog Timeout |

**Key Discoveries:**
- Complete pin mappings now available
- Comprehensive library documentation available
- Example code patterns available
- Hardware conflicts identified (LED/7-segment)
- I2C device addresses documented
- ADC channel mappings confirmed
- Timing information partially available
- Lab 3: ISR names, Timer0 formula, USART register setup, LCD custom chars, rand_n() pattern

---

## 🧪 LAB IMPLEMENTATION LEARNINGS (From Completed Labs)

### LCD / SLCD Display (Lab 3 Task A)

**AVR Address Space Error with String Literals:**
- **Problem**: Passing string literals directly to `SLCDWriteString("Hello World!")` causes: *"passing argument from pointer to non-enclosed address space"*
- **Cause**: On AVR, string literals live in Flash; `SLCDWriteString(char *pBuffer)` expects a RAM pointer
- **Fix**: Use RAM buffers before calling:
  ```c
  char buf[] = "Hello World!";
  SLCDWriteString(buf);
  ```

**SLCDWriteBuffer Correct Usage:**
- **Signature**: `SLCDWriteBuffer(unsigned char *pBuffer, unsigned char NumBytes)`
- **Wrong**: `SLCDWriteBuffer(0, 1)` — first argument must be a pointer
- **Correct**: `unsigned char ch = 0; SLCDWriteBuffer(&ch, 1);` — `ch` is the custom character slot index (0–7)

**Custom Character at Random Location:**
- Use `rand_n(n)` with Timer0 running: `TCCR0B = (1 << CS01) | (1 << CS00);`
- **Robust bounds**: Use `rand_n(3)` for rows (0–3) and `rand_n(19)` for columns (0–19) — avoids reliance on `MAX_ROW`/`MAX_COLUMN` if headers differ by build
- **Moving character**: Recalculate `row` and `col` inside the loop each iteration; clear screen, set new position, draw, delay

**Required Includes:**
- `#include <avr/io.h>` — for `TCCR0B`, `TCNT0`, `CS01`, `CS00`
- Lab 3 spec also mentions `avr/interrupt.h`, `avr/sleep.h` (needed for Tasks B/C)

**Long Message (3 Lines):**
- Spec requires 3 groups on 3 lines (rows 0, 1, 2), not 4 lines

### 7-Segment Display (Lab 2)

**Displaying Decimal 0–99 (Tens and Ones):**
- **Problem**: `SEG7WriteHex(val)` shows the value as hex (e.g. 42 → "2A")
- **Fix**: Split into tens and ones digits:
  ```c
  SEG7WriteLeft(val_0_99 / 10);   /* Tens digit */
  SEG7WriteRight(val_0_99 % 10);  /* Ones digit */
  ```
- Use for POT1 percentage (Lab 2 Task B) and temperature (Lab 2 Task D)

### Build / Toolchain Notes

- **Include case**: Some projects use `LabBoard.h` (capital B), others `Labboard.h` — may matter on case-sensitive systems
- **Delay functions**: Labboard provides `DelayMilliSec()`; AVR-GCC projects may use `_delay_ms()` from `<util/delay.h>` with `#define F_CPU 8000000UL`

**Remaining Gaps:**
- Hardware schematics still needed
- Detailed timing specifications
- Physical board layout
- Some implementation details

---

**Last Updated**: After Lab 1–3 implementation (LCD address space fix, 7-seg tens/ones, SLCDWriteBuffer, rand_n)  
**Next Steps**: Obtain hardware schematics, perform experimental timing verification, test callback signatures
