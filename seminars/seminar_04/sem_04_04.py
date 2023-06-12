# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def bubble_sort(num_list: list) -> list:
    '''
    пузырьковая сортировка
    :param num_list: list
    :return: list
    '''
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)-1):
            if num_list[j]>num_list[j+1]:
                temp = num_list[j]
                num_list[j] = num_list[j+1]
                num_list[j + 1] = temp
    return num_list

num_list = [2,5,3,6,7,8,8,6,89,7,94,7,8,9]
print(bubble_sort(num_list))
