# Сортировка файлов в указанной директории

import os
from hw_13_01 import EmptyDictionaryException, EmptyFolderException


class SortFiles:
    '''
    сортировка файлов по папкам
    '''

    def __init__(self, **kwargs):
        '''
        конструктор
        :param kwargs: именованные аргументы (возможные расширения файлов)
        '''
        # если словарь пустой, поднимаем исключение
        if not len(kwargs):
            raise EmptyDictionaryException(**kwargs)
        self.dict_ext_files = kwargs

    def sort_files(self, folder):
        '''
        сортировщик файлов по расширениями файлов
        :param folder: директория с файлами
        :return:
        '''
        try:
            # переходим в папку
            os.chdir(folder)
        except FileNotFoundError as e:
            print(f'Не верное имя директории. Возникла ошибка {e}.')
        else:
            # если директория пустая, поднимаем исключение
            if not len(os.listdir(os.getcwd())):
                raise EmptyFolderException(folder)
            # собираем список (только) файлов
            list_files = filter(lambda file_obj: os.path.isfile(file_obj), os.listdir(os.getcwd()))
            for file in list_files:
                _, ext = file.split('.')
                for sort_folder, av_ext in self.dict_ext_files.items():
                    # если папка в folder ещё не создана, создаём
                    if not os.path.exists(sort_folder):
                        os.mkdir(sort_folder)
                    # если расширение в перечне, то переносим файл в соответствующую папку в folder
                    if ext in av_ext:
                        # новое имя файла относительно папки folder
                        dest = os.path.join(sort_folder, file)
                        os.replace(file, dest)


if __name__ == '__main__':
    dict_ext_folders = {
        'text': ('txt', 'html'),
        'img': ('jpg', 'bmp'),
    }
    sorter = SortFiles(**dict_ext_folders)
    folder = 'test_folder'
    sorter.sort_files(folder)
