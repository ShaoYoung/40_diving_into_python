# итераторы и генераторы
# создание функции-генератора

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
