# Урок 15. Обзор стандартной библиотеки Python
# Модуль collections
# namedtuple

from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11), Point(2, 202, 1)]

# сортировка списка data будет выполнена сначала по левому аргументу (x), если равны, то по y и далее по z
print(sorted(data))
