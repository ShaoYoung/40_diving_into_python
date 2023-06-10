# функции

# max, min, sum

"""max(iterable, *[,key, default]) или max(arg1, arg2, *args[,key])"""
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [('Иван', 125_000), ('Николай', 96_000), ('Пётр', 109_000)]
print(max(lst_1, default='empty'))
print(max(lst_2))
print(max(lst_3, key=lambda x: x[1]))

"""min(iterable, *[,key, default]) или min(arg1, arg2, *args[,key])"""
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [('Иван', 125_000), ('Николай', 96_000), ('Пётр', 109_000)]
print(min(lst_1, default='empty'))
print(min(lst_2))
print(min(lst_3, key=lambda x: x[1]))

"""sum(iterable, /, start=0"""
my_list = [42,256,73]
print(sum(my_list))
print(sum(my_list, start=1024))

