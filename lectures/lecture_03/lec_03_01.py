# list. Создание, добавление, удаление
list_1 = list()
list_2 = list((3.14, True, "Hello"))
list_3 = []
list_4 = [3.14, True, "Hello"]

print(list_2[0])
print(list_2[-1])

list_3.append(5)
print(list_3)

list_3.extend(list_4)
print(list_3)

list_3.extend('Hello')
print(list_3)
list_3.extend(list_3)
print(list_3)

print(list_3.pop())
print(list_3.pop(0))
print(list_3.pop(-1))

print(list_3.count('l'))

print(list_3.index('l'))
print(list_3.index('l', 10, len(list_3)))
# print(f'qwerty {list_3.index(100)}')      // ошибка, т.к. элемента нет. Использовать с count.

list_3.insert(0,'first')
list_3.insert(-1,'pre-last')
print(list_3)

list_3.remove('l')
print(list_3)

