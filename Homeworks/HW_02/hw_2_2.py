# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
from math import gcd


# сокращение дроби
def fraction_reduction(fractions_num: int, fractions_den: int) -> str:
    # находим НОД
    nod = gcd(fractions_num, fractions_den)
    # если есть НОД > 1, то сокращаем дробь
    if nod > 1:
        fractions_num = fractions_num // nod
        fractions_den = fractions_den // nod
    if fractions_num == fractions_den:
        return '1'
    elif fractions_den == 1:
        return str(fractions_num)
    else:
        return f'{fractions_num}/{fractions_den}'


str_1 = input('Введите первую дробь в формате "a/b": ')
str_2 = input('Введите вторую дробь в формате "a/b": ')

# распаковываем в числители и знаменатели
num_1, den_1 = map(int, str_1.split('/'))
num_2, den_2 = map(int, str_2.split('/'))

# числители
fractions_num_sum = num_1 * den_2 + num_2 * den_1
fractions_num_mul = num_1 * num_2
# знаменатель
fractions_den = den_1 * den_2

fraction_sum = fraction_reduction(fractions_num_sum, fractions_den)
fraction_mul = fraction_reduction(fractions_num_mul, fractions_den)

print(f'{str_1} + {str_2} = {fraction_sum}')
print(f'Проверка при помощи fractions: {str_1} + {str_2} = {Fraction(str_1) + Fraction(str_2)}')
print(f'{str_1} * {str_2} = {fraction_mul}')
print(f'Проверка при помощи fractions: {str_1} * {str_2} = {Fraction(str_1) * Fraction(str_2)}')
