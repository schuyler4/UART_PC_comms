import serial
import time
import struct
import threading

baudrate = 9600

my_serial = serial.Serial('COM6', baudrate=baudrate, timeout=0.1)

def read_data():
    while True:
        try:
            data_str = my_serial.readline()
        except my_serial.serial.SerialTimeoutException:
            print('Data could not be read')
            return

        data_str = data_str.decode('utf-8')
        print(data_str)

        if(data_str == 'END'):
            break

        time.sleep(0.01)


while True:
    user_input = input('Enter a command: ')
    
    if(user_input == 'echo'):
        string = b''
        string += struct.pack('!B', 0)

        my_serial.write(string)

        read_data()
        # Start a thread running the timer function.
        time_out_thread.start()