# Проверка на существование даты.

from hw_13_01 import IncorrectValueException


def _leap(year):
    ULIAN = 4
    GRIG_1 = 400
    GRIG_2 = 100
    return year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0


def check_date(date):
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    try:
        day, month, year = map(int, date.split('.'))
    except ValueError as e:
        print(f'Некорректный ввод даты {date}. Возникла ошибка {e}')
    else:
        for value in day, month, year:
            if value < 1:
                raise IncorrectValueException(value)
        if year <= 9999 and month <= 12 and day <= 31:
            if (_leap(year) and month == 2 and day <= 29) or (month == 2 and day <= 28) or (
                    month in m_30 and day <= 30) or (month in m_31 and day <= 31):
                return True
        return False


if __name__ == '__main__':
    print(check_date('14.07.2023'))
