'''
Tests the CounterFit app connection

To run this test, ensure you have the CounterFit Virtual IoT Device app running

'''
# pylint: disable=redefined-outer-name,unused-argument

import pytest

from counterfit_connection import CounterFitConnection

def test_init_counterfit_device():
    '''
    Tests the connection. You should see the CounterFit app status change to connected
    '''
    CounterFitConnection.init('127.0.0.1', 5000)

# def test_get_sensor_bool_value():
#     '''
#     Tests reading a True boolean value from a boolean sensor on port 0
#     '''
#     CounterFitConnection.init('127.0.0.1', 5000)
#     assert CounterFitConnection.get_sensor_boolean_value(0)

# def test_read_serial_char():
#     '''
#     Tests reading a character from a serial sensor on port /dev/ttyAMA0 containing the text 'hello'
#     '''
#     CounterFitConnection.init('127.0.0.1', 5000)
#     assert CounterFitConnection.read_serial_sensor_char('/dev/ttyAMA0') == 'h'
#     assert CounterFitConnection.read_serial_sensor_char('/dev/ttyAMA0') == 'e'
#     assert CounterFitConnection.read_serial_sensor_char('/dev/ttyAMA0') == 'l'
#     assert CounterFitConnection.read_serial_sensor_char('/dev/ttyAMA0') == 'l'
#     assert CounterFitConnection.read_serial_sensor_char('/dev/ttyAMA0') == 'o'

def test_read_serial_line():
    '''
    Tests reading a line from a serial sensor on port /dev/ttyAMA0 containing the text 'hello\nworld'
    '''
    CounterFitConnection.init('127.0.0.1', 5000)
    assert CounterFitConnection.read_serial_sensor_line('/dev/ttyAMA0') == 'hello'
    assert CounterFitConnection.read_serial_sensor_line('/dev/ttyAMA0') == 'world'
