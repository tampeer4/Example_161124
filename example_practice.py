'''
Как работает все внутри, именно на пальцах логику объяснить, 
чтобы накрепко закрепилось в голове, так как сейчас что-то пишется, но без исключительного понимания
В идеале на примере из задачи по теории/практике

from datetime import datetime


class Store:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        # Родительский класс не представляет собой конкретный магазин, поэтому он всегда закрыт
        return False

    def get_info(self, date_str):
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(date_str, '%d.%m.%Y')
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class MiniStore(Store):
    def is_open(self, date):
        return date.weekday() < 5


class WeekendStore(Store):
    def is_open(self, date):
        return date.weekday() > 4


class NonStopStore(Store):
    def is_open(self, date):
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))


================================================================================
МОЖНО БЫЛО БЫ И ТАК НАПИСАТЬ

from datetime import datetime


class MiniStore:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        return date.weekday() < 5

    def get_info(self, date_str):
        date_object = datetime.strptime(date_str, '%d.%m.%Y')
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class WeekendStore:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        return date.weekday() > 4

    def get_info(self, date_str):
        date_object = datetime.strptime(date_str, '%d.%m.%Y')
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


class NonStopStore:
    def __init__(self, address):
        self.address = address

    def is_open(self, date):
        return True

    def get_info(self, date_str):
        date_object = datetime.strptime(date_str, '%d.%m.%Y')
        if self.is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {date_str} {info}'


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))
'''