from software.interface import init_serial, echo, random_numbers

#
# This function must be run with the microcontroller hardware disconnected from the PC.
#

def test_hardware_disconnected():
    my_serial = init_serial()

    try:
        assert my_serial == None
        print('Hardware disconnected test passed')
        return True
    except:
        print('Hardware disconnected test failed')
        return False

#
# The functions below must be run with the microcontroller hardware connected to the PC.
#

def test_echo():
    my_serial = init_serial()
    echo_data = echo(my_serial)

    try:
        assert 'ECHO' in echo_data
        print('Echo test passed.')
        return True
    except:
        print('Echo test failed.')
        return False


def test_random_numbers():
    my_serial = init_serial()
    x, y = random_numbers(my_serial)
    
    try:
        assert x == [0, 88, 22, 33, 4, 5, 6, 7, 8, 91]
        assert y == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        print('Random numbers test passed.')
        return True
    except:
        print('Random numbers test failed.')
        return False