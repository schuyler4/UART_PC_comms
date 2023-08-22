<h2> UART PC Comms </h2>
<h3>Rationale</h3>
In many projects I have had the needed to either log serial data from a Python script running on a PC, or 
a full back and forth communication interface between a Python program and a microcontroller. This project
is my attempt to implement some basic code that does this. 
<h3>Implementation</h3>
Both firmware that runs on the microcontroller and the Python code is included. There is somewhat of an 
implementation of a master slave protocol, with the PC the master and microcontroller the slave. 
The firmware was written for an ATMega328. I did my testing with an Adafruit Feather 328P. It may be possible
to make it work with ATMega328 Arduino boards with minimal changes. Obviously, any hardware that is used will
need to have a USB to UART bridge.