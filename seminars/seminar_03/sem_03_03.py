# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

tup = {435, 'greg', 5.6, 'grr', 4, 5, 'rgrg'}
dict_1 = {}
for item in tup:
    dict_1.setdefault(type(item), []).append(item)
    # dict_1[type(item)] = dict_1.get(type(item), []) + [item]

print(dict_1)




