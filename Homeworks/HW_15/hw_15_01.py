# Задание №6
# 📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
import os
import argparse
from collections import namedtuple
# from sys import platform


def parser():
    parser = argparse.ArgumentParser(description='Our parser')
    parser.add_argument('folder', metavar='F', type=str, nargs='*', help='Please, enter folder path.')
    args = parser.parse_args()
    print(args.folder[0])
    create_namedtuple(args.folder[0])


def log(folder_object):
    FORMAT = '{levelname:<8} - {asctime}. {msg}'
    logging.basicConfig(filename='folder_object.log', format=FORMAT, style='{', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f'Append\t{folder_object}')


def create_namedtuple(folder):
    # список полей класса
    fields = ['name', 'ext', 'flag_folder', 'parent_folder']
    # создаётся класс FolderObject
    FolderObject = namedtuple('FolderObject', fields)
    # список FolderObject (содержимое folder)
    content_list = []
    if os.path.exists(folder):
        folder_content = os.walk(folder)
        for path, folders, files in folder_content:
            # print(f'{path = } ___ {folders = } ___ {files = }')
            parent_folder = path.rsplit('\\', 1)[-1]
            for item in folders:
                folder_object = FolderObject(item, None, True, parent_folder)
                content_list.append(folder_object)
                log(folder_object)
            for item in files:
                # если файл оказался без расширения
                try:
                    file_name, file_ext = item.rsplit('.', 1)
                except ValueError:
                    file_name = item
                    file_ext = 'absent'
                folder_object = FolderObject(file_name, file_ext, False, parent_folder)
                content_list.append(folder_object)
                log(folder_object)
        print(*content_list)
    else:
        print(f'Директории {folder} не существует!')


if __name__ == '__main__':
    # folder = 'C:\\Users\\Nikita\\PycharmProjects\\40_diving_into_python\\Homeworks\\HW_14'
    # folder = 'C:\\Users\\Nikita\\PycharmProjects\\40_diving_into_python\\Homeworks'
    # folder = 'C:/Users/Nikita/PycharmProjects/40_diving_into_python/Homeworks/HW_14'
    # create_namedtuple(folder)

    # if platform == "linux" or platform == "linux2":
    #     print('linux')
    # elif platform == "darwin":
    #     print('OS X')
    # elif platform == "win32":
    #     print('Windows')
    # Если ты передать абсолютный путь в unix/windows формате в любую из библиотек (os или pathlib) и будет запущен скрипт в той же системе,
    # то он сам определит нужный формат. Вряд ли кто-то, работая например на linux, будет передавать путь в свою функцию в windows формате.
    # Но в будущем может пригодиться.

    parser()
'''
python hw_15_01.py C:/Users/Nikita/PycharmProjects/40_diving_into_python/Homeworks/HW_14
'''
