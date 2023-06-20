# Задание 2.
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 10
NUM_OF_ATTEMPTS = 3


def game(low, high, num_of_attempts):
    number = randint(low, high)
    attempt = 0
    print(
        f'Программа загадывает число от {low} до {high}. Необходимо угадать число за {attempt} попыток.')
    while attempt < num_of_attempts:
        attempt += 1
        user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
        if user_number < number:
            print('Меньше')
        elif user_number > number:
            print('Больше')
        else:
            print(f'Вы отгадали с {attempt} попытки!')
            return True
    else:
        print(f'Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.')
        return False


__all__ = ['game']

if __name__ == '__main__':
    print(game(LOWER_LIMIT, UPPER_LIMIT, NUM_OF_ATTEMPTS))

