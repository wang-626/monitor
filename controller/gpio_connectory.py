'''check datebase gpio set and set gpio value'''
from service.sql import get_gpio_status


class GpioConnector():
    '''check datebase gpio set and set gpio value'''

    def __init__(self, gpio, db):
        self.gpio = gpio
        self.db = db
        gpio.set_output()
        self.gpio_val = get_gpio_status(db)

    def set_gpio_val(self, val):
        '''set_gpio_val'''
        self.gpio_val = val
        if val == 1:
            self.gpio.set_high()
        elif val == 0:
            self.gpio.set_low()
        else:
            pass

    def check_db_gpio_set(self):
        '''check db gpio set'''
        db_gpio_set = get_gpio_status(self.db)
        if db_gpio_set != self.gpio_val:
            self.set_gpio_val(db_gpio_set)
