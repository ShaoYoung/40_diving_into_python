# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

N = 10


def check_simple(number):
    if number % 2 == 0 and number != 2:
        return False
    else:
        #     перебирать имеет смысл только до корня из number (теория чисел)
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


def gen_simple_numbers(n):
    count = 0
    yield 2
    number = 3
    while count < n - 1:
        if check_simple(number):
            yield number
            count += 1
        number += 2


print(*gen_simple_numbers(N))
