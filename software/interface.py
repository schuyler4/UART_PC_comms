'''
FILENAME: interface.py

description: This file is code for that master that runs on a PC.

Written by: Marek Newton
'''

import serial
import time
import matplotlib.pyplot as plt

baudrate = 9600
serial_port = 'COM6'
no_data_error = 10

data_start_command = 'START'
data_end_command = 'END'


# This function sets of the serial object.
def init_serial():
    try:
        my_serial = serial.Serial()
        my_serial.port = serial_port
        my_serial.baudrate = baudrate
        my_serial.timeout = 1
        
        my_serial.open()
        # For some reason, a delay is required before flushing the serial buffer.
        time.sleep(1)
        my_serial.flush()
        return my_serial
    except:
        print('Serial port could not be opened')
        return None


# This function loops through the serial data stream, reads it, and returns the data.
def read_serial_data(my_serial):
    no_data_count = 0
    received_data = []
    logging_data = False

    while True:
        try:
            data_str = my_serial.readline().decode('utf8')

            # Check if the string contains a sub string.
            if(data_str == ''):
                no_data_count += 1

                if(no_data_count > no_data_error):
                    print('No data received')
                    break
            elif(data_end_command in data_str):
                logging_data = False
                break
            elif(data_start_command in data_str):
                logging_data = True
            else:
                received_data.append(data_str)
                no_data_count = 0

        # Catch the exception and print it.
        except:
            print('Data could not be read')
            break   

    return received_data


# This function decodes the decoded binary integer. 
def sanitize_integer(string):
    cleaned_string = string.replace('\x00', '').replace('\n', '')
    decoded_integer = int(cleaned_string)
    return decoded_integer


# This function separates the stream of x and y data into two lists.
def separate_data(data):
    x = []
    y = []

    sampling_x = False
    sampling_y = False

    for data_str in data:
        if('X' in data_str):
            sampling_x = True
            sampling_y = False
        elif('Y' in data_str):
            sampling_y = True
            sampling_x = False
        else:
            if(sampling_x):
                x.append(sanitize_integer(data_str))
            elif(sampling_y):
                y.append(sanitize_integer(data_str))

    return x, y


# This function plots the random data for the user to see.
def plot_data(x, y):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


# This function runs the basic command line user interface.
def user_interface(my_serial):
    while True:
        user_input = input('Enter a command: ')
        
        if(user_input == 'echo'):
            my_serial.write(b'1')
            time.sleep(0.1)
            data = read_serial_data(my_serial)

            if(len(data) > 0):
                # Print the data without the newline character.
                print(data[0][:-1])

        elif(user_input == 'random'):
            my_serial.write(b'2')
            time.sleep(0.1)
            data = read_serial_data(my_serial)

            if(len(data) > 0):
                # Print the data without the newline character.
                x, y = separate_data(data)
                plot_data(x, y)

        elif(user_input == 'exit'):
            break
        else:
            print('Invalid command')