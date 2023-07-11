# list. Сортировка, развороты, длина
import copy

lst = [1, 5, 7, 3, 9, 2, 9]

print(sorted(lst))
print(sorted(lst, reverse=True))

lst = [1, 5, 7, 3, 9, 2, 9]
lst.sort()
print(lst)

print(list(reversed(lst)))
lst.reverse()
print(lst)

print(lst[::-1])

print(lst)
print(lst[2:5:1])
print(lst[:5:1])
print(lst[::2])
print(lst[3::2])

lst_2 = lst
lst.append('qwerty')
print(lst, lst_2)

lst.append([1,2,3])
lst_2 = lst.copy()
lst[-1].append('blabla')
print(lst, lst_2, sep=' === ')

lst_2 = copy.deepcopy(lst)
lst[-1].remove('blabla')
print(lst, lst_2, sep=' === ')

print(len(lst))
print(len(lst_2))
print(len(lst_2[-1]))




