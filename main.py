import signal
from apscheduler.schedulers.blocking import BlockingScheduler
from controller.check_connection import machine_connection
from repoitory.uart import Uart
from controller.gpio_connectory import GpioConnector
from repoitory.sql import Database
from repoitory.gpio import Gpio
from service.check_network import check_network
from dotenv import dotenv_values

config = dotenv_values(".env")


remote_db = {
    "host": config['db_host'],
    "port": 3306,
    "user": config['db_user'],
    "password": config['db_password'],
    "database": config['db_name']
}


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    PORT = "/dev/ttyS5"
    db = Database(remote_db)
    db2 = Database(remote_db)
    uart = Uart(PORT)
    gpio = Gpio(2)
    gpio_connector = GpioConnector(gpio, db)
    task = BlockingScheduler()
    task.add_job(func=machine_connection, args=[
                 uart, db2], trigger='interval', seconds=3)
    task.add_job(func=gpio_connector.check_db_gpio_set,
                 trigger='interval', seconds=10)

    print('Monitor runnig...')
    task.start()


if __name__ == "__main__":
    main()
