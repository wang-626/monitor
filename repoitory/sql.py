'''Sql entity control'''
import pymysql
from dotenv import dotenv_values

config = dotenv_values(".env")


class Database:
    def __init__(self):
        '''Initialize database data '''
        self.db = {
            "host": config['db_host'],
            "port": 3306,
            "user": config['db_user'],
            "password": config['db_password'],
            "database": config['db_name']
        }
        self.conn = None
        self.cursor = None

    def connect(self):
        '''database connect '''
        self.conn = pymysql.connect(**self.db)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        '''database disconnect '''
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_query_all(self, query):
        '''returns all the rows or None of a query result'''
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Exception as error:
            print("Error executing query:", error)
            return error

    def execute_query_one(self, query):
        '''returns a single record or None'''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except Exception as error:
            print("Error executing query:", error)
            return error

    def commit_changes(self):
        '''database commit push'''
        try:
            self.conn.commit()
            return True
        except Exception as error:
            print("Error committing changes:", error)
            self.conn.rollback()
            return error

    def insert_data(self, table, data) -> None:
        '''
        database insert value use dict format

        example:

        {
          "column1":123,

          "column2":456,
        }
        '''
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        data = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.cursor.execute(data)

    def __del__(self):
        '''close sql if sql not close'''
        if self.conn:
            self.disconnect()
