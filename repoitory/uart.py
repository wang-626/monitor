'''Control uart entity'''

import serial


class Uart:
    '''connection port and set timeout'''

    def __init__(self, port, timeout: int = 1):
        self.port = port
        self.uart = None
        try:
            self.uart = serial.Serial(port, baudrate=9600, timeout=timeout)
        except serial.SerialException:
            print(f'SerialException check port:{port}')

    def send(self, data: str):
        '''send data'''
        self.uart.write(bytes(data, 'utf-8'))

    def recive(self, size: int) -> bytes:
        '''recive data'''
        data = self.uart.read(size)
        return data

    def set_timeout(self, timeout: int) -> None:
        '''reset recive data timeout'''
        self.uart.close()
        self.uart = serial.Serial(self.port, baudrate=9600, timeout=timeout)

    def __del__(self):
        '''close port if port not close'''
        if self.uart:
            self.uart.close()
            print(f'Port {self.uart} close')
