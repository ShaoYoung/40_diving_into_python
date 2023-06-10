# функции
# lambda

def add_two_def(a, b):
    return a + b


# Это для примера. Так не делать !!!
add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3}
s_key = sorted(my_dict.items())
print(s_key)

# my_dict.items возвращает пару ключ-значение, x - это и есть пара ключ-значение. x[0] - ключ, x[1] - значение
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(s_value)
