'''Uart service'''


def test_connection(port, data: str) -> bool:
    '''
    A uart sends data to B uart.

    A uart recivce smae data or none

    return bool
    '''
    port.send(data)
    response = port.recive(4)
    return response == bytes(data, 'utf-8')
