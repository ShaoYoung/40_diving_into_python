# Задание №6
# 📌 Напишите программу, которая запрашивает год и проверяет его на високосность.
# 📌 Распишите все возможные проверки в цепочке elif
# 📌 Откажитесь от магических чисел
# 📌 Обязательно учтите год ввода Григорианского календаря
# 📌 В коде должны быть один input и один print

year = int(input('Введите год: '))

ULIAN = 4
GRIG_1 = 400
GRIG_2 = 100

check = 'не '
# условие проверки в один if
if year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0:
    check = ''

print(f'Год {year} {check}високосный')
