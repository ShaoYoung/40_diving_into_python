# Задание №3
# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итератор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

our_string = 'Однажды в студёную зимнюю пору...'
dict_comp = {item: ord(item) for item in set(our_string)}
print(dict_comp)
staff = iter(dict_comp.items())
for _ in range(5):
    print(next(staff))
