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

#define ECHO_COMMAND_CHARACTER '0'

int main(void)
{
    setup_UART();
    UART_transmit_string("RESET\n\r");

    while(1)
    {
        uint8_t command = UART_getc();
        switch(command)
        {
            case ECHO_COMMAND_CHARACTER:
                echo();
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
    UART_transmit_string("START\n\r");
    UART_transmit_string("ECHO\n\r");
    UART_transmit_string("END\n\r");
}