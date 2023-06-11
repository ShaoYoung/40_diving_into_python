# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

COUNT_SPACE = 1
user_str = input('Введите что-нибудь: ')
list_str = user_str.split()
list_str.sort()
long = 0
for item in list_str:
    if len(item) > long:
        long = len(item)
long = long + COUNT_SPACE
for i, item in enumerate(list_str, 1):
    print(f'{i}:{item:>{long}} ')

# Это можно не делать. Просто добавьте пробел явно в 18 строке
# print(f'{i}: {item:>{long}} ')

