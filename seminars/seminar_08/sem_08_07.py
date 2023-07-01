# Задание №7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import csv
import pickle

__all__ = ['csv_pickle']

def csv_pickle(csv_filename):
    with open(csv_filename, 'r', encoding='utf-8') as csv_f:
        csv_read = csv.reader(csv_f)
        pickle_string = b''
        for line in csv_read:
            pickle_string += pickle.dumps(line)
    print(f'{pickle_string = }')


if __name__ == '__main__':
    csv_filename = 'person_list.csv'
    csv_pickle(csv_filename)
