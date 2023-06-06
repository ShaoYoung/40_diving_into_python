# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
from math import gcd

# сокращение дроби
def fraction_reduction(fractions_num:int, fractions_den:int) -> str:
    # находим НОД
    nod = gcd(fractions_num, fractions_den)
    # если есть НОД > 1, то сокращаем дробь
    if nod > 1:
        fractions_num = int(fractions_num / nod)
        fractions_den = int(fractions_den / nod)
    return f'{str(fractions_num)}/{fractions_den}'

str_1 = input('Введите первую дробь в формате "a/b": ')
str_2 = input('Введите вторую дробь в формате "a/b": ')

num_1 = list(map(int, str_1.split('/')))
num_2 = list(map(int, str_2.split('/')))

# числители
fractions_num_sum = num_1[0] * num_2[1] + num_2[0] * num_1[1]
fractions_num_mul = num_1[0] * num_2[0]
# знаменатель
fractions_den = num_1[1] * num_2[1]

fraction_sum = fraction_reduction(fractions_num_sum, fractions_den)
fraction_mul = fraction_reduction(fractions_num_mul, fractions_den)

print(f'{str_1} + {str_2} = {fraction_sum}')
print(f'Проверка при помощи fractions: {str_1} + {str_2} = {Fraction(str_1) + Fraction(str_2)}')
print(f'{str_1} * {str_2} = {fraction_mul}')
print(f'Проверка при помощи fractions: {str_1} * {str_2} = {Fraction(str_1) * Fraction(str_2)}')


