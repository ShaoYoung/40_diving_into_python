# итераторы и генераторы
# Итераторы

# a = 42
# iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

print(*list_iter)   # итератор одноразовый
print(*list_iter)

list_iter = iter(data)
print(next(list_iter))
for _ in range(len(data)):
    print(next(list_iter, 'А больше нету...'))

