'''check connection and logging sql'''
from service.uart import test_connection
from repoitory.sql import Database
from datetime import datetime


def machine_connection(port):
    '''start check connection'''
    uart_connect_result = test_connection(port)
    if uart_connect_result:
        connect = 1  # 1 is connection
    else:
        connect = 0  # 0 is not connection
    table = 'test1'
    data = {
        'connect':  connect,
        'log_time': datetime.now(),
    }
    db = Database()
    db.connect()
    db.insert_data(table, data)
    db_insert_result = db.commit_changes()
    return uart_connect_result, db_insert_result
