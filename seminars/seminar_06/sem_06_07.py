# Задание 7.
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import datetime


def _leap(year):
    ULIAN = 4
    GRIG_1 = 400
    GRIG_2 = 100
    return year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0


def check_data(date):
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if (_leap(year) and month == 2 and day <= 29) or (month == 2 and day <= 28) or (
                month in m_30 and day <= 30) or (month in m_31 and day <= 31):
            return True
    return False


__all__ = ['check_data']

if __name__ == '__main__':
    print(check_data('20.06.2023'))
    # вариант через datetime и обработку исключения:
    # print(datetime.datetime.strptime('31.06.2023', "%d.%m.%Y"))
