# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл, хранящий список словарей в табличный csv файл.
# 📌 Для тестирования возьмите pickle версию файла из предыдущей задачи.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv

__all__ = ['pickle_csv']

# DictWriter
def pickle_csv(pickle_filename):
    csv_filename = f'{pickle_filename.rsplit(".", 1)[-2]}.csv'
    print(f'{csv_filename = }')
    with(open(csv_filename, "w", encoding="utf-8", newline='') as csv_f,
         open(pickle_filename, "rb") as pickle_f
         ):
        new_obj = pickle.load(pickle_f)
        print(f'{new_obj = }')
        # ключи словаря - заголовки столбцов
        headers = [key for key in new_obj[0].keys()]
        print(f'{headers = }')
        csv_write = csv.DictWriter(csv_f, fieldnames=headers)
        # записываем заголовки
        csv_write.writeheader()
        # записываем список словарей
        csv_write.writerows(new_obj)


if __name__ == '__main__':
    pickle_filename = 'person_list.pickle'
    pickle_csv(pickle_filename)
