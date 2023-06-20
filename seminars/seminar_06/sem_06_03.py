# Задание 3.
# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint
from sys import argv


def game(low=0, high=10, num_of_attempts=3):
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
    print(argv)
    _, *params = argv
    print(game(*map(int, params)))

# python sem_06_03.py 0 10 3

