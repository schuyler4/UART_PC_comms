import sys

from .test_software import test_sanitize_integer, test_separate_data
from .test_system import test_hardware_disconnected, test_echo, test_random_numbers

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        if(sys.argv[1] == 'software'):
            t1 = test_sanitize_integer()
            t2 = test_separate_data()
            if(t1 and t2):
                print('SOFTWARE TESTS PASS')
        elif(sys.argv[1] == 'hardware_connected'):
            t1 = test_echo()
            t2 = test_random_numbers()
            if(t1 and t2):
                print('HARDWARE CONNECTED TESTS PASS')
        elif(sys.argv[1] == 'hardware_disconnected'):
            if(test_hardware_disconnected()):
                print('HARDWARE DISCONNECTED TESTS PASS')
    else:
        print('No test suite specified.')
