# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

our_string = 'Однажды в студёную зимнюю пору...'
dict_comp = {item: ord(item) for item in set(our_string)}