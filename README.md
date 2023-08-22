<h2> UART PC Comms </h2>
<h3>Rationale</h3>
In many projects I have needed serial communication between a Python script running on a PC and 
a microcontroller. This project is my attempt to implement some basic code that does this. 
<h3>Implementation</h3>
Both firmware that runs on the microcontroller and the Python code is included. There is somewhat of an 
implementation of a master slave protocol, with the PC the master and microcontroller the slave. 
The firmware was written for an ATMega328. I did my testing with an Adafruit Feather 328P. It may be possible
to make it work with ATMega328 Arduino boards or similar with minimal changes. Obviously, any hardware that is 
used will need a USB to UART bridge.