# ДЗ
# Задание.
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
# Уточнение:
# Доделать два метода из задания №5
# 3 задачи
# Создать собственные исключения, поместить их в отдельный модуль

# Модуль с описанием классов исключений

class BaseException(Exception):
    pass


class IncorrectSideException(BaseException):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Вы ввели сторону прямоугольника {self.side}. Возникла ошибка {self.__class__.__name__}, ' \
               f'т.к. нельзя создавать прямоугольник со сторонами отрицательной длины.'


class EmptyDictionaryException(BaseException):
    def __init__(self, **dict_ext_files):
        self.dict_ext_files = dict_ext_files

    def __str__(self):
        return f'Вы передали пустой словарь возможных расширений файлов {self.dict_ext_files}. ' \
               f'Возникла ошибка {self.__class__.__name__}, т.к. недостаточно информации для сортировки файлов.'


class EmptyFolderException(BaseException):
    def __init__(self, folder):
        self.folder = folder

    def __str__(self):
        return f'Директория {self.folder} пустая. Возникла ошибка {self.__class__.__name__}, т.к. сортировать нечего.'


class IncorrectValueException(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Не корректный ввод даты. Возникла ошибка {self.__class__.__name__}. Дат со значением {self.value} не бывает.'
