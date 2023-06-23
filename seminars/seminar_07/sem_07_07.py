# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
# TEXT
# IMG

def sort_file(dir_name, dict_files):
    # TODO walk не нужен

    list_files = list(os.walk(dir_name))

    for file in list_files[0][2]:
        _, ext = file.split('.')
        print(ext)
        for key, value in dict_files.items():
            os.mkdir(key)

            if ext in value:

        # print(file)

    # print(list_files)




if __name__ == '__main__':
    dict_files = {
        'text':('txt'),
        'img':('jpg')
    }
    dir_name = os.getcwd() + '\\7_source'
    sort_file(dir_name, dict_files)










