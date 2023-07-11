# словарь, dict

a = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
b = dict(one=42, two=3.14, ten='Hello, world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello, world!')])
print(a == b == c)
print(a is b is c)

my_dict = {'one': 1, 'two': 2, 'three': 3}
x = 10
my_dict['ten'] = x
print(my_dict)

TEN = 'ten'
print(my_dict['two'])
print(my_dict[TEN])
# print(my_dict[1])     // ошибка, т.к. ключа 1 нет
key = '1'
print(my_dict.get(key, f'нет ключа {key}'))




