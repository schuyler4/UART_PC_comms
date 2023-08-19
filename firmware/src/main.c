//
// FILENAME: main.c
//
// UART PC Comms Basic Firmware
//
// Description: This is the firmware side of the UART PC Comms. This code 
// sends data over UART when requested by the PC. 
//
// Written by: Marek Newton
//

#define F_CPU 8000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

#include "UART.h"
#include "main.h"

#define TRANSMIT_DELAY 100

#define ECHO_COMMAND_CHARACTER '1'
#define RANDOM_NUMBERS_CHARACTER '2'

#define RANDOM_NUMBERS_LENGTH 10

uint8_t random_numbers1[RANDOM_NUMBERS_LENGTH] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
uint8_t random_numbers2[RANDOM_NUMBERS_LENGTH] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

int main(void)
{
    setup_UART();

    while(1)
    {
        uint8_t command = UART_receive_character();
        switch(command)
        {
            case ECHO_COMMAND_CHARACTER:
                echo();
                break;
            case RANDOM_NUMBERS_CHARACTER:
                random_numbers();
                break;
            default:
                break;
        }
    }

    // The program should never return.
    return 1;
}

void echo(void)
{
    _delay_ms(100);
    UART_transmit_string("START\n");
    UART_transmit_string("ECHO\n");
    UART_transmit_string("END\n");
}

void random_numbers(void)
{
    UART_transmit_string("START\n");
    for(uint8_t i = 0; i < 2; i++)
    {
        if(i == 0)
        {
            UART_transmit_string("X\n");
        }
        else
        {
            UART_transmit_string("Y\n");
        }

        for(uint8_t j = 0; j < RANDOM_NUMBERS_LENGTH; j++)
        {
            if(i == 0)
            {
                UART_transmit_uint8_t(random_numbers1[j]);
            }
            else
            {
                UART_transmit_uint8_t(random_numbers2[j]);
            }
            UART_transmit_string("\n");
        }
    }
    UART_transmit_string("END\n");
}