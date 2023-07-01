# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

#  samodurOFF yesterday (30.06.2023)
# Что-то сложно. Как я говорил на семинаре, лучше создать json сущность в виде списка словарей. После этого его можно будет преобразовать как в строку pickle, так и в файл csv.
# При этом структура каждого словаря может быть такая.
#
# {
#       'obj': <имя объекта>,
#       'parent': <имя родителя>,
#       'obj_type': <тип объекта(папка или файл)>,
#       'size': <размер объекта>,
# }
# Для каждого объекта в директории нужно создать такой словарь и поместить их всех в один список. После этого всего то и нужно, что записать этот список словарей сначала в файл json, а потом файл pickle. Потом при помощи класса DictWriter записать в файл csv. В вот и всё.
# Вот пример функции, которая принимает на вход список словарей с указанной структурой и записывают его в указанные файлы.
#
# def save_to_files(data):
#     with (
#         open('data.json', 'w', encoding='utf-8') as json_f,
#         open('data.csv', 'w', newline='', encoding='utf-8') as csv_f,
#         open('data.pickle', 'wb') as pickle_f,
#     ):
#         json.dump(data, json_f, indent=4, ensure_ascii=False)
#         pickle.dump(data, pickle_f)
#
#         csv_write = csv.DictWriter(csv_f, fieldnames=[*data[0]])
#         csv_write.writeheader()
#         csv_write.writerows(data)

import os
import json
import csv
import pickle
import pandas


def recursion_folder(folder, json_filename, csv_filename, pickle_filename):
    # обходим с нижнего уровня
    tree_list = os.walk(folder, topdown=False)
    tree = {}
    sub_tree = {}
    prev_path_len = 0
    min_path_len = 0
    for path, folders, files in tree_list:
        print(f'{path = } ___ {folders = } ___ {files = }')

        # словарь файлов в директории
        files_in_folder = {file: f'{os.stat(os.path.join(path, file)).st_size} bytes' for file in files}
        file_sizes = 0
        for file in files_in_folder:
            file_sizes += os.stat(os.path.join(path, file)).st_size
            print(f'{file} - {os.stat(os.path.join(path, file)).st_size}')

        last_folder = path.rsplit('\\', 1)[-1]
        # print(f'{last_folder = }')
        upper_folder = path.rsplit('\\', 2)[-2]
        # upper_folders.add(upper_folder)
        # print(f'{upper_folders = } ___ {upper_folder = } ___ {last_folder = }')
        print(f'{upper_folder = } ___ {last_folder = }')

        path_len = len(path.split('\\'))
        print(f'{path_len = } ___ {prev_path_len = } ___ {min_path_len = }')

        if prev_path_len and prev_path_len < path_len:
            print('Субдиректория')
            sub_tree.update({upper_folder: {last_folder: files_in_folder}})
        elif prev_path_len and path_len < min_path_len:
            print('На уровень выше')

            for file, filesize in files_in_folder.items():
                sub_tree.update({file: filesize})

            if sub_tree:
                tree.update({last_folder: sub_tree.copy()})
                print(f'{tree = } ___ {sub_tree = } ___ {files_in_folder = }')
                sub_tree.clear()
            else:
                print(f'{sub_tree = } пустой')
                tree_copy = tree.copy()
                tree.clear()
                print(f'{last_folder = }')
                tree.update({last_folder: tree_copy})

            print(f'{tree = }')

        else:
            if last_folder in sub_tree.keys():
                print(f'Ключ {last_folder} уже есть')
                sub_tree[last_folder].update(files_in_folder)
            else:
                sub_tree.update({last_folder: files_in_folder})
        print(f'{sub_tree = }')

        min_path_len = min(path_len, prev_path_len)
        prev_path_len = path_len

        print()

    print("Дерево:")
    print(f'\n{tree = }')

    with(
        open(pickle_filename, "wb") as pickle_f,
        open(json_filename, 'w', encoding='utf-8') as json_f
    ):
        json.dump(tree, json_f)
        pickle.dump(tree, pickle_f)

        df = pandas.DataFrame(tree)
        df.to_csv(csv_filename)
        # dict_keys = tree.keys()
        # csv_write = csv.DictWriter(csv_f, fieldnames=dict_keys)
        # csv_write.writeheader()
        # csv_write.writerows(tree)


if __name__ == '__main__':
    # абсолютный путь к директории на два уровня выше текущей
    # folder = os.path.abspath('..\\..')
    # абсолютный путь к директории на один уровень выше текущей
    # folder = os.path.abspath('..\\')
    # folder = os.getcwd()
    # папка test
    json_filename = 'hw_08_01.json'
    csv_filename = 'hw_08_01.csv'
    pickle_filename = 'hw_08_01.pickle'
    folder = os.path.join(os.getcwd(), 'test')
    print(f'{folder = }')
    recursion_folder(folder, json_filename, csv_filename, pickle_filename)
