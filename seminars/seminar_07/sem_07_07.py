# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os

__all__ = ['sort_files']


def sort_files(folder, dict_ext_files):
    '''
    сортировщик файлов по расширениями
    :param folder: директория с файлами
    :param dict_ext_files: словарь (ключ - папка, значение - возможные расширения файлов для папки)
    :return:
    '''
    # переходим в папку
    os.chdir(folder)
    # собираем список (только) файлов
    list_files = filter(lambda file_obj: os.path.isfile(file_obj), os.listdir(folder))
    # print(list_files)
    for file in list_files:
        _, ext = file.split('.')
        # print(ext)
        for sort_folder, av_ext in dict_ext_files.items():
            # если папка в folder ещё не создана, создаём
            if not os.path.exists(sort_folder):
                os.mkdir(sort_folder)
            # если расширение в перечне, то переносим в соответствующую папку в folder
            if ext in av_ext:
                # новое имя файла относительно папки folder
                dest = os.path.join(sort_folder, file)
                # print(dest)
                os.replace(file, dest)


if __name__ == '__main__':
    dict_ext_folders = {
        'text': ('txt', 'html'),
        'img': ('jpg', 'bmp')
    }
    folder = os.path.join(os.getcwd(), '7_6')

    sort_files(folder, dict_ext_folders)
