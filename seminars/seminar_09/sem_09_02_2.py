# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

# вариант без синтаксического сахара

from random import randint

def deco(func):
    def wrapper(number, num_of_attempts):
        if not 1 <= number <= 100:
            print(f'Параметр {number = } не в диапазоне')
            number = randint(1,100)
        if not 1 <= num_of_attempts <= 10:
            print(f'Параметр {num_of_attempts = } не в диапазоне')
            num_of_attempts = randint(1,10)
        func(number, num_of_attempts)
    return wrapper


# @deco
def game(number, num_of_attempts):
    attempt = 0
    while attempt < num_of_attempts:
        attempt += 1
        user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
        if user_number < number:
            print('Вы вводите меньше')
        elif user_number > number:
            print('Вы вводите больше')
        else:
            print(f'Вы отгадали с {attempt} попытки!')
            return True
    else:
        print(f'Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.')
        return False


if __name__ == '__main__':
    number = 100
    num_of_attempts = 5
    # game(number, num_of_attempts)
    print(game.__name__)
    game = deco(game)
    print(game.__name__)
    # game(number, num_of_attempts)
