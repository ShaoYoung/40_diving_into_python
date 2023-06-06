# Задание №8
# 📌 Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# 📌 Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input('Сколько рядов у ёлки? '))
for row in range(1, rows + 1):
    count_star = row * 2 - 1
    count_space = rows * 2 - 1 - count_star
    # переделано на целочисленное деление
    spruce_row = ' ' * (count_space // 2) + '*' * count_star + ' ' * (count_space // 2)
    print(spruce_row)
