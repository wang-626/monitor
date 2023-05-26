'''Sql service'''

from datetime import datetime


def get_gpio_status(db) -> bool:
    '''get gpio table value'''
    db.connect()
    query = 'SELECT status FROM gpio ORDER BY id DESC'
    return db.query_one(query)[0]


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

def sqlite_initialize(db):
    '''insert gpio table value'''
    db.connect()
    db.sql('CREATE TABLE IF NOT exists gpio(status, set_time DATETIME)')
    db.sql('CREATE TABLE IF NOT exists orangepi_connect(connect, log_time DATETIME)')
    return db.commit_changes()

def find_column_name(db, table_name):
    columns = db.query_all(f"PRAGMA table_info(gpio)")
    column_names = []
    for column in columns:
        if column[1].lower() != 'id':
            column_names.append(column[1])
    return ",".join(column_names)