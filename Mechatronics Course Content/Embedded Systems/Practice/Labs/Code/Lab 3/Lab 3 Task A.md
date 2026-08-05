# Lab 3 Task A

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab3_TaskA.c` · [[Lab Board Knowledge]]

```c
/*
 * Lab3_TaskA.c
 * ENEL712 Embedded Systems Design - Lab Week 3: LCD, USART, ISRs
 * Task A: LCD usage
 *
 * Goals: Hello World, long message on 3 lines, custom character at random location
 * Hardware: AT90USB1287 Lab Board, 4x20 LCD on I2C (PD0/PD1, 0x28)
 */

#include <avr/io.h>
#include <Labboard.h>

/* Custom character: 5x8 pixels, 8-byte array (5 bits per row, MSB unused) */
static const unsigned char customChar[8] = {
    0b00000100,
    0b00001010,
    0b00010001,
    0b00010001,
    0b00001010,
    0b00000100,
    0b00000100,
    0b00000100
};

/* rand_n(n): returns 0..n using TCNT0 (Timer0 must be running) */
unsigned int rand_n(unsigned int n)
{
    return (unsigned int)(TCNT0 % (n + 1));
}

int main(void)
{
    unsigned int row, col;

    /* Start Timer0 for rand_n() - prescaler 1024 */
    TCCR0B = (1 << CS01) | (1 << CS00);

    SLCDInit();
    SLCDClearScreen();
    SLCDDisplayOn();

    /* 1. Hello World */
    SLCDSetCursorPosition(0, 0);
    {
        char buf[] = "Hello World!";
        SLCDWriteString(buf);
    }

    DelayMilliSec(2000);

    /* 2. Long message on 3 lines (spec: 3 groups on lines 0, 1, 2) */
    SLCDClearScreen();
    SLCDSetCursorPosition(0, 0);
    {
        char buf1[] = "First group of words";
        char buf2[] = "Second group here";
        char buf3[] = "Third group of text";
        SLCDWriteString(buf1);
        SLCDSetCursorPosition(1, 0);
        SLCDWriteString(buf2);
        SLCDSetCursorPosition(2, 0);
        SLCDWriteString(buf3);
    }

    DelayMilliSec(2000);

    /* 3. Custom character - moves to random locations (row 0-3, col 0-19) */
    SLCDLoadCustomCharacter(0, (unsigned char *)customChar);

    {
        unsigned char ch = 0;
        while (1)
        {
            SLCDClearScreen();
            row = rand_n(3);      /* 4 rows: 0-3 */
            col = rand_n(19);      /* 20 cols: 0-19 */
            SLCDSetCursorPosition((unsigned char)row, (unsigned char)col);
            SLCDWriteBuffer(&ch, 1);
            DelayMilliSec(500);
        }
    }
    return 0;
}
```
