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
for row in range(1, rows+1):
    count_star = row * 2 - 1
    count_space = rows * 2 - 1 - count_star
    spruce_row = ' ' * int(count_space/2) + '*' * count_star + ' ' * int(count_space/2)
    print(spruce_row)