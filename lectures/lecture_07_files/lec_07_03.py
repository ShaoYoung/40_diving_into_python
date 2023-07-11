# Файлы и файловая система

with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
# print(f.write('Пока'))  # файл уже закрыт


with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')  # пустая строка

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(100):  # чтение порциями по 100 символов
        print(res)

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(100):  # чтение порциями по 100 символов
        print(res)

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:      # построчное считывание в цикле
        # возможные варианты, результат одинаковый
        print(line, end='')
        print(line[:-1])
        print(line.replace('\n', ''))