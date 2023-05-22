'''Test uart connection'''
import unittest
from unittest.mock import Mock
from repoitory.uart import Uart
from service.uart import test_connection


class TestUartConnectionJudgment(unittest.TestCase):
    '''Test test_connection funciotn '''
    mock_uart = Mock(spec=Uart)  # 模擬的uart

    def test_uart_connectionr(self):
        '''Test uart is connection A <-> B '''
        self.mock_uart.recive.return_value = b'true'  # uart有成功連線
        self.assertEqual(test_connection(self.mock_uart, 'true'), True)

    def test_uart_disconnected(self):
        '''Test uart is not connection A X B '''
        self.mock_uart.recive.return_value = b''  # uart沒有成功連線
        self.assertEqual(test_connection(self.mock_uart, 'true'), False)


if __name__ == '__main__':
    unittest.main()
