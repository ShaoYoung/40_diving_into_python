# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

list_1 = [3, 5, 357, 8, 8, 7, 5, 456, 7, 67, 33, 1, 2, 3, 56, 8, 7, 0, 3, 8, 7, 456]
list_2 = []
for i in range(len(list_1)):
    if list_1[i] % 2:
        list_2.append(i+1)
print(list_2)


