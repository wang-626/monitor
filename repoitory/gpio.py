'''gpio entity control'''

import sys
sys.path.append(
    '/usr/lib/python3.9/site-packages/wiringpi-2.60.1-py3.9-linux-aarch64.egg/')  # 3.9以上需要

import wiringpi
from wiringpi import GPIO


class Gpio():
    def __init__(self, pin: int) -> None:
        '''Initialize gpio '''
        wiringpi.wiringPiSetup()
        self.pin = pin
        self.mode = 'None'
        self.status = f'Pin:{str(self.pin)}  Mode:{str(self.mode)}'

    def set_output(self) -> None:
        '''set gpio mode output'''
        wiringpi.pinMode(self.pin, GPIO.OUTPUT)
        self.mode = 'OUT'

    def set_input(self) -> None:
        '''set gpio mode input'''
        wiringpi.pinMode(self.pin, GPIO.IN)
        self.mode = 'IN'

    def set_high(self) -> None:
        '''set gpio output value'''
        wiringpi.digitalWrite(self.pin, 1)

    def set_low(self) -> None:
        '''set gpio output value'''
        wiringpi.digitalWrite(self.pin, 0)
