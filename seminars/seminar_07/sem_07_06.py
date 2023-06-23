# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from random import choice, choices, randint

LETTERS = 'qwertyuiopasdfghjklzxcvbnm'

__all__ = ['make_dif_ext_files_to_folder']


def make_files_to_folder(ext, folder, min_length=6, max_length=30, min_byte=256, max_byte=4096, count_files=42):
    for _ in range(count_files):
        filename = ''.join(choices(LETTERS, k=randint(min_length, max_length))) + '.' + ext
        full_filename = os.path.join(folder, filename)
        if os.path.exists(full_filename):
            print(f'Файл {full_filename} уже существует')
        else:
            content = ''
            for _ in range(randint(min_byte, max_byte)):
                content += choice(LETTERS)
            with open(full_filename, 'wb') as f:
                f.write(bytes(content, 'utf-8'))


def make_dif_ext_files_to_folder(dict_ext, folder):
    '''
    Генератор файлов в указанную директорию
    :param dict_ext: словарь с расширениями и количествами файлов
    :param folder: директория, куда будут генерироваться файлы
    :return:
    '''
    # проверяем существование директории
    if not os.path.exists(folder):
        print(f'Директории {folder} на данном ПК не существует. Она будет создана.')
        os.mkdir(folder)
    for ext, count in dict_ext.items():
        make_files_to_folder(ext, folder, min_length=3, max_length=8, min_byte=10, max_byte=50, count_files=count)


if __name__ == '__main__':
    # словарь расширений и количества файлов
    dict_ext = {
        'txt': 4,
        'jpg': 5,
        'bmp': 2,
        'mp3': 1,
        'html': 3,
    }
    # директория, куда будут сохраняться сгенерированные файлы
    folder = os.path.join(os.getcwd(), '7_6')
    make_dif_ext_files_to_folder(dict_ext, folder)
