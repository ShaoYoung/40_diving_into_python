# итераторы и генераторы
# set comprehensions
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)
for char in my_setcomp:
    print(char, end=' ')
print()


x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(len(x), len(y))
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)}\n{res}')

# dict comprehensions
my_dictcomp = {i:chr(i) for i in range(97, 123)}
print(my_dictcomp)
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
