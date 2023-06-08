# Множества, set, frozenset

my_set = {1,2,3,4,5,6,7,8,9}
print(my_set)
my_f_set = frozenset((1,2,3,4,5,6,7,8,9))
print(my_f_set)

my_set.add(9)
print(my_set)

my_set.remove(5)
print(my_set)

# my_set.remove(10)     // ошибка, т.к. 10 нет в множестве
# print(f'{my_set}')

my_set.discard(10)      # // элемента нет и ошибки нет
print(f'{my_set}')

your_set = {2,11,89,4,7}
new_set = my_set.intersection(your_set)
# аналогичная запись
# new_set = my_set & your_set
print(new_set)

new_set = my_set.union(your_set)
# аналогичная запись
# new_set = my_set | your_set
print(new_set)


new_set = my_set.difference(your_set)
# аналогичная запись
# new_set = my_set - your_set
print(new_set)




