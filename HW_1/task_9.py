# Задание №9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке


# список строк с \n
space = ' ' * 25
print(f'\n{space}ТАБЛИЦА УМНОЖЕНИЯ\n')

# таблица - список строк
mul_table = list()
# делаем строку из каждого произведения
for i in range(2, 10):
    for j in range(2, 11):
        if len(str(i * j)) == 1:
            space_1 = ' '
            space_2 = space_1
        elif j == 10:
            space_1 = ''
            space_2 = ''
        else:
            space_1 = ' '
            space_2 = ''
        mult = f'{i} X {j}{space_1} = {space_2}{i * j}'
        mul_table.append(mult)
# выводим таблицу
for i in range(2):
    for j in range(0, 9):
        for k in range(j + i * 36, 28 + j + i * 36, 9):
            print(mul_table[k], end='       ')
        print()
    print()