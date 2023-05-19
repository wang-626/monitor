from controller.check_connection import machine_connection
from repoitory.uart import Uart


if __name__ == "__main__":
    PORT = "COM4"
    uart_connect_result, db_insert_result = machine_connection(Uart(PORT))
    print(uart_connect_result, db_insert_result)
