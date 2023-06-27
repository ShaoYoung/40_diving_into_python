# Задание №4
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.


import csv
import json


def csv_json(csv_file, json_file):
    with(open(json_file, "w", encoding="utf-8") as json_f,
         open(csv_file, "r", newline='', encoding="utf-8") as csv_f
         ):
        csv_file = csv.reader(csv_f)
        # json_dict = {}
        json_list = []
        for i, line in enumerate(csv_file, 1):
            id, level, name = line
            if id.isdigit():
                while len(id) < 10:
                    id += '0'
                print(f'{id = }')
            name.capitalize()
            hash_name = hash(id + name)
            print(f'{hash_name = }')
            # json_dict.update({f'{i} строка': {'level': level, 'id': id, 'name': name, 'hash_name': hash_name}})
            json_list.append({f'{i} строка': {'level': level, 'id': id, 'name': name, 'hash_name': hash_name}})
            # print(f'{json_dict = }')
            print(f'{json_list = }')
        # ensure_ascii=False - вывод символов как они есть (не в кодировке ASCII)
        # json.dump(json_dict, json_f, indent=1, ensure_ascii=False)
        json.dump(json_list, json_f, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    csvfile = 'person.csv'
    jsonfile = 'person_new.json'
    csv_json(csvfile, jsonfile)
