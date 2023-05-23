from apscheduler.schedulers.blocking import BlockingScheduler
from controller.check_connection import machine_connection
from repoitory.uart import Uart
import signal


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    PORT = "COM4"
    task = BlockingScheduler()
    task.add_job(func=machine_connection, args=[
                 Uart(PORT)], trigger='interval', seconds=3)

    print('runnig...')
    task.start()
