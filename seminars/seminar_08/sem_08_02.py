# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключом для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа (в пределах одного уровня доступа).
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os


def code(filename):
    # если файл существует, открываем и записываем содержимое в словарь
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            my_dict = json.load(f)
    else:
        # иначе создаём новый словарь, где ключи - уровни доступа
        my_dict = {str(level): {} for level in range(1, 8)}
    print(f'{my_dict = }')

    while True:
        name, id_person, level, *_ = input("Введите имя, личный идентификатор и уровень доступа через пробел: ").split()
        # если идентификатора нет в ключах словаря, то добавляем пару {идентификатор : имя} в словарь
        if id_person not in my_dict[level].keys():
            my_dict[level].update({id_person: name})
            break
        else:
            print('Идентификатор не уникален')
    print(f'{my_dict = }')

    with open(filename, "w", encoding="utf-8") as f:
        # записываем словарь в json-файл с отступом=1
        json.dump(my_dict, f, indent=1)


if __name__ == '__main__':
    filename = 'person.json'
    code(filename)
