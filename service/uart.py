'''Uart service'''


def test_connection(port):
    '''
    A uart sends data to B uart.

    A uart recivce smae data or none

    return bool
    '''
    port.send('true')
    response = port.recive(4)
    return response == b'true'
