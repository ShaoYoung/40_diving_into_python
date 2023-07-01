# Задание №5
# 📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.


import pickle
import json
import os

__all__ = ['json_pickle']

def json_pickle(folder):
    if os.path.exists(folder):
        # список файлов с расширением json
        json_files = list(filter(lambda file_obj: os.path.isfile(file_obj) and file_obj.rsplit('.', 1)[-1] == 'json',
                                 os.listdir(folder)))
        print(f'{json_files = }')
        for json_file in json_files:
            pickle_name, _ = json_file.rsplit('.',1)
            pickle_name += '.pickle'
            # print(pickle_name)
            with(open(json_file, "r", encoding="utf-8") as json_f,
                 open(pickle_name, "wb") as pickle_f
                 ):
                json_dict = json.load(json_f)
                print(f'{json_dict = }')
                pickle.dump(json_dict, pickle_f)


if __name__ == '__main__':
    # получаем текущую директорию
    folder = os.getcwd()
    json_pickle(folder)
