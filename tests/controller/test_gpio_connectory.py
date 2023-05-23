'''Test whether the result of connecting or not connecting to uart is correct'''
import unittest
from unittest.mock import Mock
from repoitory.sql import Database
from controller.gpio_connectory import GpioConnector


class GPIO():
    '''mock gpio'''
    def execute_query_one(self):
        '''mock'''

    def set_high(self):
        '''mock'''

    def set_low(self):
        '''mock'''

    def set_output(self):
        '''mock'''


class TestGpioConnector(unittest.TestCase):
    '''Test whether the result of connecting or not connecting to uart is correct'''

    def test_init_check_db_gpio_set(self):
        '''test sql return 0 or 1 result'''
        mock_db = Mock(spec=Database)  # 模擬的db
        mock_gpio = Mock(GPIO)  # 模擬的gpio
        mock_db.execute_query_one.return_value = 0  # sql回傳0
        gpio = GpioConnector(mock_gpio, mock_db)
        self.assertEqual(gpio.gpio_val, 0)
        mock_db.execute_query_one.return_value = 1  # sql回傳1
        gpio = GpioConnector(mock_gpio, mock_db)
        gpio.check_db_gpio_set()
        self.assertEqual(gpio.gpio_val, 1)

    def test_set_gpio_val(self):
        pass


if __name__ == '__main__':
    unittest.main()
