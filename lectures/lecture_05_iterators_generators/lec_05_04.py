# итераторы и генераторы
# Генераторы

# генераторные выражения
my_gen = (chr(i) for i in range(97, 123))
print(my_gen)
for char in my_gen:
    print(char, end=' ')
print()

# два вложенных цикла с условиями включения элемента в последовательность
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(len(x), len(y))
mult = list(i + j for i in x if i % 2 != 0 for j in y if j != 1)
print(f'{len(mult)}\n{mult}')
