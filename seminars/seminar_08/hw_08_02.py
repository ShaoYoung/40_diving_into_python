# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import sys
sys.path.append('..\\..\\Homeworks\\HW_08')

from hw_08_01 import recursion_folder

__all__ = ['rec_folder']

def rec_folder(folder, json_filename, csv_filename, pickle_filename):
    recursion_folder(folder, json_filename, csv_filename, pickle_filename)



