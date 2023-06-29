# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.

from functools import wraps


COUNT = 3


def param(count):
    def deco(func):
        res_list = []
        @wraps(func)
        def wrapper(*args):
            for _ in range(count):
                res = func(*args)
                res_list.append(res)
        return wrapper

    return deco


@param(COUNT)
def my_func(*args):
    return (args)

@param(COUNT)
def my_func_1(*args):
    return (args)


if __name__ == '__main__':
    # count = 5
    my_func('Hello world')
    my_func_1('Hello')
