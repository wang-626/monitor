'''Test sql service'''
import unittest
from repoitory.sql import Database
from service.sql import get_gpio_status, set_gpio_status
from dotenv import dotenv_values

config = dotenv_values(".env")

remote_db = {
    "host": config['db_host'],
    "port": 3306,
    "user": config['db_user'],
    "password": config['db_password'],
    "database": config['db_name']
}


class TestServiceSql(unittest.TestCase):
    '''Test get_gpio_status, set_gpio_status  '''

    def test_set_gpio_status(self):
        '''Test sql set/get gpio status '''
        db = Database(remote_db)
        self.assertEqual(set_gpio_status(db, 1), 1)
        result = get_gpio_status(db)
        self.assertEqual(result, 1)
        set_gpio_status(db, 0)
        result = get_gpio_status(db)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
