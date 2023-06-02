# Задание №7
# 📌 Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# 📌 Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

import math

while True:
    user_input = input('Введите число от 1 до 999: ')
    if user_input.isdigit():
        number = int(user_input)
        if number in range(1, 1000):
            break
    print('Не корректный ввод! Повторите.')

num_digits = int(math.log10(number)) + 1

match num_digits:
    case 1:
        print('Введена цифра.')
        print(f'Квадрат числа {number} равен {number * number}')
    case 2:
        print('Введено двузначное число.')
        print(f'Произведение цифр числа {number} равно {(number // 10) * (number % 10)}')
    case 3:
        print('Введено трёхзначное число.')
        one = number % 10
        ten = number // 10 % 10
        hundred = number // 100
        mirror_number = hundred + ten * 10 + one * 100
        print(f'Зеркальное отображение числа {number} - {mirror_number}')