'''check connection and logging sql'''
from datetime import datetime
from service.uart import test_connection


def machine_connection(port, db):
    '''start check connection'''
    uart_connect_result = test_connection(port, 'true')
    if uart_connect_result:
        connect = 1  # 1 is connection
    else:
        connect = 0  # 0 is not connection
    table = 'orangepi_connect'
    data = {
        'connect':  connect,
        'log_time': datetime.now(),
    }
    db.connect()
    db.insert_data(table, data)
    db_insert_result = db.commit_changes()
    return uart_connect_result, db_insert_result
