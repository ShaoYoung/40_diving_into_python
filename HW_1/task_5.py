# Задание №5
# 📌 Работа в консоли в режиме интерпретатора Python.
# 📌 Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# 📌 Используйте while и if.
# 📌 Попробуйте разные значения e и n.

N = 100
count = 1
elem_sum = 0
E = 4
while count <= N:
    count += 1
    # if count % E == 0:
    #     continue
    # elif count % 2 == 0:
    # заменил на условие через and и E != 0, т.к. надо исключить кратные E
    if count % 2 == 0 and count % E != 0:

        elem_sum += count
        print(count, end=' ')
print()
print(elem_sum)