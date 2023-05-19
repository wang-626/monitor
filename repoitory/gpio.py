'''gpio entity control'''

import sys
sys.path.append('/usr/lib/python3.9/site-packages/wiringpi-2.60.1-py3.9-linux-aarch64.egg/')
import wiringpi
from wiringpi import GPIO
wiringpi.wiringPiSetup();

class Gpio():
    def __init__(self, port):
        '''Initialize gpio '''
        self.port = int(port)
        self.Status = ''

    def output(self, value):
        '''set gpio output'''
        wiringpi.pinMode(self.port, GPIO.OUTPUT)
        self.Status = 'Port' + str(self.port) + ' ouput ' +str(value)

    def input(self):
        '''set gpio input'''
        wiringpi.pinMode(self.port, GPIO.IN)
        self.Status = ' Input ' + str(self.port)
        return GPIO.input(self.port)
