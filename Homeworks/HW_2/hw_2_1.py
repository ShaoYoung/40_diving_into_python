# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

SYSTEM_16 = 16


def convert(number: int, system: int) -> str:
    sign = ''
    # проверка на отрицательное число
    if number == 0:
        return '0'
    elif number < 0:
        sign = '-'
        number = abs(number)
    # символы шестнадцатеричной системы счисления, которых нет в десятичной системе
    hex_notation = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    # список строк
    temp = list()
    while number > 0:
        remainder = number % system
        if remainder in hex_notation:
            remainder = hex_notation[remainder]
        temp.append(str(remainder))
        number = number // system
    temp.append(sign)
    # разворот списка строк
    temp.reverse()
    return ''.join(temp)

num = int(input('Введите целое число: '))
print(f'Число {num} в шестнадцатеричной системе {convert(num, SYSTEM_16)}')
print(f'Проверка стандартной функцией hex {hex(num)}')
