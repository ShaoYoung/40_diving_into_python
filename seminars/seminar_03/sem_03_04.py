# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

NUM_REP = 2
list_1 = [3, 5, 357, 8, 8, 7, 5, 456, 456, 7, 67, 33, 1, 2, 3, 56, 8, 7, 0, 3, 8, 7]
for item in set(list_1):
# for item in list_1:
    if list_1.count(item) == NUM_REP:
        for _ in range(NUM_REP):
            list_1.remove(item)
print(list_1)
