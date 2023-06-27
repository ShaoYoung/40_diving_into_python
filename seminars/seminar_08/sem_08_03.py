# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.


import csv
import json


def json_csv(jsonfile):
    csvfile = 'person.csv'
    with(open(jsonfile, "r", encoding="utf-8") as json_f,
         open(csvfile, "w", newline='', encoding="utf-8") as csv_f
         ):
        json_dict = json.load(json_f)
        print(f'{json_dict = }')
        # строки для csv-файла
        rows = []
        for level, in_dict in json_dict.items():
            for id, name in in_dict.items():
                rows.append({'id': id, 'level': int(level), 'name': name})

        print(f'{rows = }')

        csv_write = csv.DictWriter(csv_f, fieldnames=['id', 'level', 'name'])
        # запись заголовка (то, что в [fieldnames])
        csv_write.writeheader()
        # записываем матрицу (список списков) в csv-файл
        csv_write.writerows(rows)


if __name__ == '__main__':
    jsonfile = 'person.json'
    json_csv(jsonfile)
