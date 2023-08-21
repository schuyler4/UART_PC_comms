'''
FILENAME: test_software.py

description: This file tests the pure software functions that do
not require the microcontroller hardware to be connected.

Written by: Marek Newton
'''

from software.interface import sanitize_integer, separate_data

def test_sanitize_integer():
    try:
        assert sanitize_integer('\x000\n') == 0
        assert sanitize_integer('\x0082\n') == 82
        assert sanitize_integer('\x002\n') == 2
        print('sanitize_integer test passed')
        return True
    except:
        print('sanitize_integer test failed')
        return False

def test_separate_data():
    pass