# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
#

import os
import sys

sys.path.append('..\\..\\Homeworks\\HW_07\\')
from hw_07_02 import rename_files as hw_rename

__all__ = ['rename_files']


def rename_files(new_name, source_ext, new_ext, source_folder):
    '''
    групповое переименовывание файлов. вызывает функцию из модуля hw_07_02. сделано для формирования пакета для работы с файлами в одном каталоге.
    :param new_name:
    :param source_ext:
    :param new_ext:
    :param source_folder:
    :return:
    '''
    hw_rename(new_name, source_ext, new_ext, source_folder)


if __name__ == '__main__':
    new_name = '==='
    source_ext = 'jpg'
    new_ext = 'png'
    folder = os.path.join(os.getcwd(), 'folder_02')
    rename_files(new_name, source_ext, new_ext, folder)
