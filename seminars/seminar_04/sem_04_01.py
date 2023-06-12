# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.
import string

text = 'Однажды в студёную зимнюю пору я из лесу вышел был сильный мороз'

def split_text(text):

    text = text.split()
    text.sort()
    print(text)
    for i, word in enumerate(text, 1):
        print(f'{word: >10}')

split_text(text)



