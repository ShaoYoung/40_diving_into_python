# Задание №4_1
# Функция получает на вход список чисел.
# Отсортируйте список по убыванию суммы цифр

def sort_list(num_list):
    our_dict = {}
    for item in num_list:
        sum_item = sum(map(int, str(item)))
        our_dict[item] = sum_item
    our_dict = sorted(our_dict, key = lambda sum_num: our_dict[sum_num], reverse=True)
    return our_dict

num_list = [25,52,34,60,71,82,83,6]

print(sort_list(num_list))
