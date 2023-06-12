# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# * учесть отрицательную индексацию (оба индекса отрицательные)

OUR_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
START = -9
END = -1

def task_6(our_list, start, end):
    if start < 0 and end < 0:
        start = len(our_list) + start
        end = len(our_list) + end + 1
    if start < 0:
        start = 0
    if end > len(our_list):
        end = len(our_list)
    sum_list = 0
    for i in range(start, end):
        sum_list += our_list[i]
    return sum_list


print(task_6(OUR_LIST, START, END))
