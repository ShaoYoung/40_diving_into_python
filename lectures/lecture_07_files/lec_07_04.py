# Файлы и файловая система

text = 'Функция combinations() модуля itertools возвращает итератор со всеми возможными комбинациями элементов входной последовательности iterable.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    # write возвращает число - сколько символов было записано в файл
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')


text = ['Функция combinations() модуля itertools ', 'возвращает итератор со всеми возможными комбинациями ', 'элементов входной последовательности iterable.']
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))

with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)

with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        # вариант выделения конца и начало строк
        print(line, end='***\n##', file=f)

