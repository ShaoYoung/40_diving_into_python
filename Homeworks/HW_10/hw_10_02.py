# Задание 2
# 📌 Возьмите любую задачу из прошлых семинаров (например сериализация данных), которую вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задача должна решаться через вызов методов экземпляра.

# Замечания преподавателя. Можно было еще раздробить этот код, создав защищенные или приватные методы.

import os


class SortFiles:
    '''
    сортировка файлов по папкам
    '''

    def __init__(self, **kwargs):
        '''
        конструктор
        :param kwargs: именованные аргументы (возможные расширения файлов)
        '''
        self.dict_ext_files = kwargs

    def sort_files(self, folder):
        '''
        сортировщик файлов по расширениями файлов
        :param folder: директория с файлами
        :return:
        '''
        # если переданная папка существует
        if os.path.exists(folder):
            # переходим в папку
            os.chdir(folder)
            # print(f'{os.getcwd() = }')
            # собираем список (только) файлов
            list_files = filter(lambda file_obj: os.path.isfile(file_obj), os.listdir(os.getcwd()))
            for file in list_files:
                _, ext = file.split('.')
                # print(ext)
                for sort_folder, av_ext in self.dict_ext_files.items():
                    # если папка в folder ещё не создана, создаём
                    if not os.path.exists(sort_folder):
                        os.mkdir(sort_folder)
                    # если расширение в перечне, то переносим файл в соответствующую папку в folder
                    if ext in av_ext:
                        # новое имя файла относительно папки folder
                        dest = os.path.join(sort_folder, file)
                        # print(dest)
                        os.replace(file, dest)
        else:
            print(f'Папки {folder} не существует!')


if __name__ == '__main__':
    dict_ext_folders = {
        'text': ('txt', 'html'),
        'img': ('jpg', 'bmp'),
    }
    sorter = SortFiles(**dict_ext_folders)
    folder = 'test_folder'
    sorter.sort_files(folder)
