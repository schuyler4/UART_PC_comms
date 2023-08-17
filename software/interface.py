import serial
import time

baudrate = 9600
serial_port = 'COM6'
no_data_error = 10

data_start_command = 'START'
data_end_command = 'END'

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


def read_serial_data(my_serial):
    no_data_count = 0
    received_data = []
    logging_data = False

    while True:
        try:
            data_str = my_serial.readline().decode('utf-8')

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


def user_interface(my_serial):
    while True:
        user_input = input('Enter a command: ')
        
        if(user_input == 'echo'):
            my_serial.write(b'1')
            time.sleep(0.1)
            read_serial_data(my_serial)
        elif(user_input == 'exit'):
            break
        else:
            print('Invalid command')


my_serial = init_serial()

if(my_serial == None):
    exit()

if __name__ == '__main__':
    user_interface(my_serial)