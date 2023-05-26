'''Test sql service'''
import unittest
from repoitory.sql import MysqlDb, SqliteDb
from service.sql import get_gpio_status, set_gpio_status, sqlite_initialize
from dotenv import dotenv_values

config = dotenv_values('.env')

remote_db = {
    'host': config['db_host'],
    'port': 3306,
    'user': config['db_user'],
    'password': config['db_password'],
    'database': config['db_name']
}


class TestServiceSql(unittest.TestCase):
    '''Test get_gpio_status, set_gpio_status  '''

    def test_set_gpio_status(self):
        '''Test sql set/get gpio status '''
        db = MysqlDb(remote_db)
        self.assertEqual(set_gpio_status(db, 1), 1)
        result = get_gpio_status(db)
        self.assertEqual(result, 1)
        set_gpio_status(db, 0)
        result = get_gpio_status(db)
        self.assertEqual(result, 0)

    def test_sqlite_initialize(self):
        db = SqliteDb('local.db')
        result = sqlite_initialize(db)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
