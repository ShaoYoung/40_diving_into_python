# Задание №7
# 📌 Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# 📌 Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

# import math

MIN_INPUT = 1
MAX_INPUT = 999

while True:
    user_input = input(f'Введите число от {MIN_INPUT} до {MAX_INPUT}: ')
    if user_input.isdigit():
        number = int(user_input)
        if number in range(MIN_INPUT, MAX_INPUT + 1):
            break
    # без print пользователю будет трудно понять, почему ввод числа зацикливается
    print('Не корректный ввод! Повторите.')

# Определение разрядности, используя операции с числами (через десятичный логарифм)
# num_digits = int(math.log10(number)) + 1

# Определение разрядности, используя операции со строками
num_digits = len(user_input)

text = ''
match num_digits:
    case 1:
        text = f'Введена цифра. Квадрат числа {number} равен {number * number}.'
    case 2:
        text = f'Введено двузначное число. Произведение цифр числа {number} равно {(number // 10) * (number % 10)}.'
    case 3:
        text = f'Введено трёхзначное число. Зеркальное отображение числа {number} - {number // 100 + (number // 10 % 10) * 10 + (number % 10) * 100}.'
print(text)
