# ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def path_name_extension(absolute_path: str) -> tuple:
    '''
    Принимает на вход строку — абсолютный путь до файла, возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
    :param absolute_path: str
    :return: tuple
    '''
    *path, file_with_ext = absolute_path.split('/')
    path = '/'.join(path)
    name, extension = file_with_ext.split('.')
    return path, name, extension


my_string = 'C:/Users/Nikita/Desktop/Python_Manual/Самоучитель_Python.pdf'
print(path_name_extension(my_string))
