<h3> UART PC Comms </h3>
This is basic firmware and software for communication between a microcontroller and a PC using the microcontroller's UART interface.
The software is a basic command line python program, and the firmware is written for an ATmega328 on a specific development board. 
The communication mostly follows a master slave protocol. The master, which is the PC, sends a command, and the slave, which is the 
microcontroller, responds with some data.