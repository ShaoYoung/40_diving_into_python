# Задание №5
# Напишите программу, которая выводит
# на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# Вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение лучше многострочное (почему?)

def game():
    for i in range(1, 101):
        if not (i % 15):
            yield 'FizzBuzz'
        elif not (i % 5):
            yield 'Buzz'
        elif not (i % 3):
            yield 'Fizz'
        else:
            yield i


print(*game())
# iter_game = iter(game())
# while iter_game:
#     print(next(iter_game))
