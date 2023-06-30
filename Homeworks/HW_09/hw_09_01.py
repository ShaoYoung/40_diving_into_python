# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса


import json
import csv
import os
from random import randint
from functools import wraps

MIN_QUANTITY = 100
MAX_QUANTITY = 1000
MAX_NUMBER_ABS = 100


def generator_csv():
    equ_quantity = randint(MIN_QUANTITY, MAX_QUANTITY)
    # для теста
    # equ_quantity = 2
    # генератор троек случайных чисел
    triple_list = [[randint(-MAX_NUMBER_ABS, MAX_NUMBER_ABS), randint(-MAX_NUMBER_ABS, MAX_NUMBER_ABS),
                    randint(-MAX_NUMBER_ABS, MAX_NUMBER_ABS)] for _ in range(equ_quantity)]
    # print(triple_list)
    filename = 'triple_list.csv'
    with open(filename, 'w', newline='') as f_csv:
        csv_write = csv.writer(f_csv)
        csv_write.writerows(triple_list)


def triple_from_csv(func):
    def wrapper():
        file_csv = 'triple_list.csv'
        with open(file_csv, 'r', newline='') as f_csv:
            csv_read = csv.reader(f_csv, quoting=csv.QUOTE_NONNUMERIC)
            for a, b, c in csv_read:
                # если a не равно нулю (иначе будет деление на ноль)
                if a:
                    func(a, b, c)
                else:
                    print(f'{a = }, делить на ноль нельзя!')

    return wrapper


def save_to_json(func):
    @wraps(func)
    def wrapper(*args):
        file_json = f'{func.__name__}.json'
        if os.path.exists(file_json):
            with open(file_json, 'r', encoding='utf-8') as fj:
                list_file = json.load(fj)
        else:
            list_file = []
        a, b, c = args
        result = func(a, b, c)
        # проверка на комплексные корни. необходима, т.к. json не работает с комплексными числами
        if isinstance(result[0], complex):
            result = f'Действительных корней нет. Комплексные корни {result}'
        list_file.append({
            'параметры': {
                'a': int(a),
                'b': int(b),
                'c': int(c)
            },
            'корни': result
        })
        file_json = f'{func.__name__}.json'
        with open(file_json, 'w', encoding='utf-8') as f_json:
            json.dump(list_file, f_json, indent=1, ensure_ascii=False)

    return wrapper


@triple_from_csv
@save_to_json
def find_roots(a=0, b=0, c=1):
    d = b ** 2 - 4 * a * c
    # print(f'Дискриминант = {d}')
    x_1 = (-b + pow(d, 0.5)) / (2 * a)
    x_2 = (-b - pow(d, 0.5)) / (2 * a)
    # print(f'Корни квадратного уравнения {x_1}, {x_2}')
    return (x_1, x_2)


if __name__ == '__main__':
    generator_csv()
    find_roots()
