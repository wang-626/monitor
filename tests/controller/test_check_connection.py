'''Test whether the result of connecting or not connecting to uart is correct'''
import unittest
from unittest.mock import Mock
from repoitory.uart import Uart
from repoitory.sql import MysqlDb
from controller.check_connection import machine_connection
from dotenv import dotenv_values

config = dotenv_values('.env')


class TestUartConnection(unittest.TestCase):
    '''Test whether the result of connecting or not connecting to uart is correct'''

    db = MysqlDb({
        'host': config['db_host'],
        'port': 3306,
        'user': config['db_user'],
        'password': config['db_password'],
        'database': config['db_name']
    })
    

    def test_uart_connectionr(self):
        '''uart connectionr'''
        mock_uart = Mock(spec=Uart) # 模擬的uart
        mock_uart.recive.return_value = b'true'  # uart有成功連線
        uart_connect_result, db_insert_result = machine_connection(mock_uart, self.db)
        self.assertEqual(uart_connect_result, True)
        self.assertEqual(db_insert_result, True)
        results = self.db.query_one('SELECT * FROM orangepi_connect ORDER BY id desc limit 1')
        self.assertEqual(results[1], 1) #連線成功資料庫結果因該為1

    def test_uart_disconnected(self):
        '''uart disconnected'''
        mock_uart = Mock(spec=Uart) # 模擬的uart
        mock_uart.recive.return_value = b''  # uart沒有成功連線
        uart_connect_result, db_insert_result = machine_connection(mock_uart, self.db)
        self.assertNotEqual(uart_connect_result, True)
        self.assertEqual(db_insert_result, True)
        results =self.db.query_one('SELECT * FROM orangepi_connect ORDER BY id desc limit 1')
        self.assertEqual(results[1], 0) #連線失敗資料庫結果因該為0



if __name__ == '__main__':
    unittest.main()
