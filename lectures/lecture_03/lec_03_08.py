# словарь, dict

my_dict = {'one': 1, 'two': 2, 'three': 3}

spam = my_dict.setdefault('five')
print(f'{spam=}\t\t\t{my_dict=}')

eggs = my_dict.setdefault('six', 6)
print(f'{eggs=}\t\t\t{my_dict=}')

new_spam = my_dict.setdefault('two', 6)
print(f'{new_spam=}\t\t\t{my_dict=}')

print(my_dict.keys())
for key in my_dict.keys():
    print(key, end=', ')
print()

for key in my_dict:
    print(key, end=', ')
print()

for value in my_dict.values():
    print(value, end=', ')

for key, value in my_dict.items():
    print(f'{key=: <5} {value=} ')
print()

print(my_dict.popitem())

print(my_dict.pop('two'))

print(my_dict)

my_dict.update(dict(six=6))
print(my_dict)

new_dict = my_dict | dict(ten=10)
print(new_dict)





