'''Test sql service'''
import unittest
from datetime import datetime
from service.sql import get_gpio_status, set_gpio_status


class TestServiceSql(unittest.TestCase):
    '''Test get_gpio_status, set_gpio_status  '''

    def test_set_gpio_status(self):
        '''Test sql set/get gpio status '''
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertEqual(set_gpio_status(1), 1)
        result = get_gpio_status()
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2].strftime("%Y-%m-%d %H:%M"), log_time)
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        set_gpio_status(0)
        result = get_gpio_status()
        self.assertEqual(result[1], 0)


if __name__ == '__main__':
    unittest.main()
