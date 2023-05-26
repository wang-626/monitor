'''Test sql connection'''
import unittest
from datetime import datetime
from repoitory.sql import MysqlDb
from repoitory.sql import SqliteDb
from dotenv import dotenv_values

config = dotenv_values('.env')

remote_db = {
    'host': config['db_host'],
    'port': 3306,
    'user': config['db_user'],
    'password': config['db_password'],
    'database': config['db_name']
}


class TestSql(unittest.TestCase):
    '''Test sql function'''

    def test_mysql_insert_query(self):
        '''Test sql insert and query'''
        db = MysqlDb(remote_db)
        db.connect()
        table = 'orangepi_connect'
        tmp_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'connect': 1,
            'log_time': tmp_time,
        }
        db.insert_data(table, data)
        db.commit_changes()
        query = f'SELECT * FROM {table} ORDER BY log_time desc'
        results = db.query_one(query)
        self.assertEqual(
            results[2].strftime('%Y-%m-%d %H:%M:%S'),
            tmp_time)  # sql最後一筆資料跟寫入資料是否相同
        
    def test_sqlite_insert_query(self):
        '''Test sql insert and query'''
        db = SqliteDb('local.db')
        db.connect()
        table = 'orangepi_connect'
        tmp_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'connect': 1,
            'log_time': tmp_time,
        }
        db.insert_data(table, data)
        db.commit_changes()
        query = f'SELECT * FROM {table} ORDER BY log_time desc'
        results = db.query_one(query)
        self.assertEqual(results[1], tmp_time)  # sql最後一筆資料跟寫入資料是否相同


if __name__ == '__main__':
    unittest.main()
