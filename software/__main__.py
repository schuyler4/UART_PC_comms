'''
FILENAME: __main__.py

description: This code executes the master user interface when the software is run.

Written by: Marek Newton
'''

from .interface import user_interface, init_serial

if __name__ == '__main__':
    my_serial = init_serial()

    # Exit the program if the serial device is not connected to the PC.
    if(my_serial == None):
        exit()

    user_interface(my_serial)