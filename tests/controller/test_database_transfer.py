'''Test sqlite database transfer mysql'''
import unittest
from repoitory.sql import MysqlDb, SqliteDb
from controller.database_transfer import database_transfer
from service.sql import sqlite_initialize
from dotenv import dotenv_values

config = dotenv_values('.env')

local_db = SqliteDb('local.db')

mysql_db = MysqlDb({
    'host': config['db_host'],
    'port': 3306,
    'user': config['db_user'],
    'password': config['db_password'],
    'database': config['db_name']
})

sqlite_initialize(local_db)

local_db.insert_data('gpio', {
    'status': 1,
    'set_time': '2011-11-11 00:00:00'
})
local_db.commit_changes()


class TestDatabaseTransfer(unittest.TestCase):
    '''Test sqlite database transfer mysql'''

    def test_database_transfer(self):
        '''test database transfer'''
        sqlite_results = local_db.query_one(
            "SELECT count(*) FROM gpio")
        self.assertEqual(sqlite_results[0] >= 1, True)
        database_transfer(local_db, mysql_db, ['gpio'])
        sqlite_results = local_db.query_one(
            "SELECT count(*) FROM gpio")
        mysql_results = mysql_db.query_one(
            "SELECT * FROM gpio ORDER BY id desc")
        print(mysql_results)
        self.assertEqual(sqlite_results[0], 0)
        self.assertEqual(mysql_results[1], 1)
        self.assertEqual(mysql_results[2], '2011-11-11')


if __name__ == '__main__':
    unittest.main()
