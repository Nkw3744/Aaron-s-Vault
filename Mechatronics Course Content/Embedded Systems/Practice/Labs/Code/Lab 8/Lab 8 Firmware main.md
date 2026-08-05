# Lab 8 Firmware main

> [!info] Course material
> [[Embedded Systems Practice Index|Back]] · Source: `main.c` · [[File Handling and Serial Ports]] · [[GUI and Event-Driven Programming]]

```c
/*
 * MICROCHIP STUDIO FLASH
 * main.c
 * Created: 5/5/2026 2:51:37 PM
 *  Author: vfy4520
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <string.h>

#define F_CPU_HZ 8000000UL
#define BAUD 9600UL
#define UBRR1_VALUE ((F_CPU_HZ/(16UL*BAUD))-1UL)

// LEDs are wired to PORTC on the lab board (PC0-PC4 = dice 0-4)
#define LED_DDR  DDRC
#define LED_PORT PORTC
#define LED_MASK 0x1F   // lower 5 bits, one per die

// Buffer to collect incoming characters until a full line arrives
static char    rx_buf[16];
static uint8_t rx_idx = 0;

// Used by the TX interrupt to send a single byte (kept from original)
volatile uint8_t tx_b;
volatile uint8_t tx_ready = 1;

ISR(USART1_RX_vect)
{
    char c = UDR1;

    if (c == '\n' || c == '\r')
    {
        // We got a full line, null-terminate and process it
        rx_buf[rx_idx] = '\0';
        if (strcmp(rx_buf, "HELLO") == 0)
        {
            const char* resp = "HELLO\n";
            for (uint8_t i = 0; resp[i]; i++)
            {
                // Wait until the transmit register is empty before sending each byte
                while (!(UCSR1A & (1<<UDRE1)));
                UDR1 = resp[i];
            }
        }
        else if (rx_idx == 6 &&
                 rx_buf[0]=='L' && rx_buf[1]=='E' &&
                 rx_buf[2]=='D' && rx_buf[3]==':')
        {
            // Parse the two hex characters into a byte
            uint8_t hi = rx_buf[4];
            uint8_t lo = rx_buf[5];
            hi = (hi >= 'A') ? hi - 'A' + 10 : hi - '0';
            lo = (lo >= 'A') ? lo - 'A' + 10 : lo - '0';

            // Write the bitmask to PORTC to light the correct LEDs
            LED_PORT = ((hi << 4) | lo) & LED_MASK;
        }

        // Reset buffer index ready for the next command
        rx_idx = 0;
    }
    else if (rx_idx < sizeof(rx_buf) - 1)
    {
        // Not a newline yet — keep buffering the character
        rx_buf[rx_idx++] = c;
    }
}

// TX interrupt unchanged from original — sends one queued byte then disables itself
ISR(USART1_UDRE_vect)
{
    if (!tx_ready) {
        UDR1 = tx_b;
        tx_ready = 1;
    }
    UCSR1B &= ~(1<<UDRIE1);
}

int main(void)
{
    // Set up USART1 baud rate registers
    UBRR1H = (UBRR1_VALUE>>8);
    UBRR1L = (UBRR1_VALUE&0xFF);

    // 8-bit data, no parity, 1 stop bit
    UCSR1C = (1<<UCSZ11)|(1<<UCSZ10);

    // Enable receiver, transmitter, and RX interrupt
    UCSR1B = (1<<RXEN1)|(1<<TXEN1)|(1<<RXCIE1);

    // Set PC0-PC4 as outputs for the 5 LEDs, start with all off
    LED_DDR  |= LED_MASK;
    LED_PORT &= ~LED_MASK;

    sei();
    set_sleep_mode(SLEEP_MODE_IDLE);
    while(1) sleep_mode();  // sleep until next interrupt, saves power
}
```
