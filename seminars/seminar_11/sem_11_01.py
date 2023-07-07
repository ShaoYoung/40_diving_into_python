# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyString(str):
    '''Класс Моя Строка'''
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creation_time = time.asctime()
        return instance


if __name__ == '__main__':
    author = 'Student'
    writing = 'Однажды в студёную зимнюю пору...'
    str_1 = MyString(writing, author)
    print(f'{str_1 = }')
    print(f'{str_1.author = }')
    print(f'{str_1.creation_time = }')
    print(help(MyString))


