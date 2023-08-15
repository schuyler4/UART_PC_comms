//
// FILENAME: UART.c
//
// description: This file has all the functionality to transmit and receive data
// over UART. 
//
// Written by Marek Newton
//

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#ifndef F_CPU
#define F_CPU 8000000UL
#endif

#define BAUD 9600
#define MYUBRR (((F_CPU / (BAUD * 16UL))) - 1)

char* int_to_string(int number)
{
    int max_digits = (int)log10(number) + 2;
    char* string = malloc(max_digits + 2 * sizeof(char));
    sprintf(string, "%d", number);
    return string;
}

// sets all the registers that are needed for UART communication
void setup_UART(void)
{
    // set baud rate 
    UBRR0H = (unsigned char)(MYUBRR>>8);
    UBRR0L = (unsigned char)MYUBRR;
    // enable receiver and transmitter
    UCSR0B = (1<<RXEN0)|(1<<TXEN0);
    // Set frame format: 8data, 2stop bit
    UCSR0C = (1<<USBS0)|(3<<UCSZ00);
}

// transmits a single character on the UART stream
void UART_transmit_char(char data)
{
    // Wait for empty transmit buffer
    while (!( UCSR0A & (1<<UDRE0)));
    // Put data into buffer, sends the data
    UDR0 = data;
}

// transmits an array of characters over UART
void UART_transmit_string(char *string)
{
    unsigned int i;
    while(1)
    {
        char character = *(string + i);
        UART_transmit_char(character);

        if(character == '\0')
        {
            break;
        }
        i++;
    }
}

void UART_transmit_int(int number)
{
    int max_digits = (int)log10(number) + 2;
    char* string = malloc(max_digits + 2 * sizeof(char));
    sprintf(string, "%d", number);

    for(int i = 0; i < max_digits; i++)
    {
        UART_transmit_char(*(string + i));
    }

    free(string);
}

char UART_getc(void)
{
    // wait for data
    while(!(UCSR0A & (1 << RXC0)));

    // return data
    return UDR0;
}

int UART_get_int(void)
{
    // wait for data
    while(!(UCSR0A & (1 << RXC0)));

    // return data
    return UDR0;
}