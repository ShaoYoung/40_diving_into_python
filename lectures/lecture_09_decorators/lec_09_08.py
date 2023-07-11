# Декораторы

import random

def count(func):
    counter = 0
    def wrapper(text):
        nonlocal counter
        func(text)
        counter += 1
        print(f'Функция вызывалась {counter} раз')

    return wrapper

@count
def print_text(text):
    print(text)

if __name__ == '__main__':
    text = '123'
    print_text(text)
    print_text(text)
    print_text(text)

