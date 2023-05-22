'''Test whether the result of connecting or not connecting to uart is correct'''
import unittest
from unittest.mock import Mock
from repoitory.uart import Uart
from controller.check_connection import machine_connection


class TestUartConnection(unittest.TestCase):
    '''Test whether the result of connecting or not connecting to uart is correct'''

    def test_uart_connectionr(self):
        '''uart connectionr'''
        mock_uart = Mock(spec=Uart) # 模擬的uart
        mock_uart.recive.return_value = b'true'  # uart有成功連線
        uart_connect_result, db_insert_result = machine_connection(mock_uart)
        self.assertEqual(uart_connect_result, True)
        self.assertEqual(db_insert_result, True)

    def test_uart_disconnected(self):
        '''uart disconnected'''
        mock_uart = Mock(spec=Uart) # 模擬的uart
        mock_uart.recive.return_value = b''  # uart沒有成功連線
        uart_connect_result, db_insert_result = machine_connection(mock_uart)
        self.assertNotEqual(uart_connect_result, True)
        self.assertEqual(db_insert_result, True)


if __name__ == '__main__':
    unittest.main()
