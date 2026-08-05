# Lab 3 Task A LCD

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `Lab3_TaskA_LCD.c` · [[Lab Board Knowledge]]

```c
#define F_CPU 8000000UL
#include <LabBoard.h>
#include <avr/io.h>
#include <util/delay.h>

unsigned int rand_n(unsigned int n)
{
      return (unsigned int)(TCNT0 % (n + 1));
}

int main(void)
{
      char line1[] = "My name is Amber";
      char line2[] = "I am hungry";
      char line3[] = "I need a drink";
      char line4[] = "Hello World!";

      unsigned char customChar[8] =
      {
            0b00001,
            0b00010,
            0b01000,
            0b10000,
            0b01010,
            0b00100,
            0b00010,
            0b00001
      };

      unsigned char row;
      unsigned char col;

      TCCR0B = (1 << CS01) | (1 << CS00);
      
            
      SLCDInit();
      SLCDClearScreen();
      SLCDDisplayOn();



      SLCDSetCursorPosition(0,0);
      SLCDWriteString(line4);

      _delay_ms(2000);

      SLCDClearScreen();

      SLCDSetCursorPosition(0,0);
      SLCDWriteString(line1);

      SLCDSetCursorPosition(1,0);
      SLCDWriteString(line2);

      SLCDSetCursorPosition(2,0);
      SLCDWriteString(line3);

      _delay_ms(2000);

      SLCDClearScreen();

      SLCDLoadCustomCharacter(0, customChar);

      while (1)
      {
            row = rand_n(3);
            col = rand_n(20);

            SLCDClearScreen();
            SLCDSetCursorPosition(row, col);
            SLCDWriteBuffer(0, 1);

            _delay_ms(500);
      }
}
```
