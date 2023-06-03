# Задание №9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

# уложился в 9 строк кода с учётом вывода заголовка
print(f'\n\t\t\t\t\t\tТАБЛИЦА УМНОЖЕНИЯ\n')
for i in (0, 4):
    for j in range(2, 11):
        for k in range(2 + i, 6 + i):
            space = ' ' if len(str(k * j)) == 1 else ''
            mul = f'{k} X {j}  = {k * j}' if j == 10 else f'{k} X {j}   = {space}{k * j}'
            print(mul, end='       ')
        print()
    print()
