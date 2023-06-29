# Задание №5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.

import os
import json
from random import randint
count = 3

from sem_09_04 import param as repeat
from sem_09_02 import deco as control
from sem_09_03 import deco as save_json

@repeat(2)
@save_json
@control
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
    game(1000, 2)