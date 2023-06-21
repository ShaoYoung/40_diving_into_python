# Файлы и файловая система

text = ['Функция combinations() модуля itertools ', 'возвращает итератор со всеми возможными комбинациями ',
        'элементов входной последовательности iterable.']
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell())     # файл уже закрыт


last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    # передвинули курсор на позицию before
    print(f'{f.seek(before, 0) = }')
    # и записали text
    f.write('\n'.join(text))

last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    # передвинули курсор на позицию before
    print(f.seek(before, 0))
    # и обрезали файл
    f.truncate()

size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))

