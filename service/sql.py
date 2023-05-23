'''Sql service'''

from repoitory.sql import Database
from datetime import datetime


def get_gpio_status(db) -> bool:
    '''get gpio table value'''
    db.connect()
    query = 'SELECT * FROM gpio ORDER BY id DESC'
    return db.execute_query_one(query)


def set_gpio_status(db, status: int):
    '''insert gpio table value'''
    table = 'gpio'
    data = {
        'status': status,
        'set_time': datetime.now(),
    }
    db.connect()
    db.insert_data(table, data)
    db_insert_result = db.commit_changes()
    return db_insert_result