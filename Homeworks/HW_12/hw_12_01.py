# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from numpy import average

MIN_GRADE = 2
MAX_GRADE = 5
MIN_TEST = 0
MAX_TEST = 100


class Descriptor:
    def __init__(self, *args):
        # если создаётся экземпляр grade или test
        if args:
            self.min_value, self.max_value = args

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


    # Этот код тоже напрашивается для отдельного метода или отдельного класса-дескриптора.
    # Сначала так и сделал, но потом посчитал, что используется один раз и отказался
    def __set__(self, instance, value):
        # если фамилия, имя или отчество
        if isinstance(value, str):
            if not (value[0].isupper() and value.isalpha()):
                raise ValueError(f'Строка {value} должна начинаться с заглавной буквы и/или состоять только из букв')
            setattr(instance, self.param_name, value)
        # если оценка
        else:
            self.validate(value)
            setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше или равно {self.max_value}')


class Student:
    surname = Descriptor()
    name = Descriptor()
    second_name = Descriptor()
    grade = Descriptor(MIN_GRADE, MAX_GRADE)
    test = Descriptor(MIN_TEST, MAX_TEST)

    def __init__(self, surname, name, second_name, filename):
        self.surname = surname
        self.name = name
        self.second_name = second_name
        # Дневник - словарь
        self.diary = {lesson: {'grade': None, 'tests': []} for lesson in self.csv_read(filename)}

    def set_grade(self, lesson: str, grade: int):
        self.grade = grade
        self.validate_lesson(lesson)
        self.diary[lesson]['grade'] = self.grade

    def set_test(self, lesson: str, test: int):
        self.test = test
        self.validate_lesson(lesson)
        self.diary[lesson]['tests'].append(self.test)

    def validate_lesson(self, lesson):
        if lesson not in self.diary.keys():
            raise ValueError(f'Предмет {lesson} отсутствует в перечне предметов, загруженных из файла')

    def get_avg_lesson_tests(self):
        return {lesson: average(self.diary[lesson]['tests']) if self.diary[lesson]['tests'] else 0 for lesson in
                self.diary.keys()}

    def get_avg_lessons(self):
        # Значения с None не учитываем
        return average([self.diary[lesson]['grade'] for lesson in self.diary.keys() if self.diary[lesson]['grade']])

    def __str__(self):
        return (f'{self.surname} {self.name} {self.second_name}')

    def csv_read(self, filename: str):
        '''Чтение csv-файла с названиями предметов. Возвращает список предметов.'''
        lessons = []
        with open(filename, 'r', newline='', encoding='utf-8') as f_read:
            csv_file = csv.reader(f_read)
            for line in csv_file:
                lessons.extend(line)
        return lessons


def csv_write(filename: str, lessons: list):
    '''Запись csv-файла с названиями предметов'''
    with open(filename, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.writer(f_write)
        csv_write.writerow(lessons)

# Отличная работа.
# Как я уже сказал, можно сделать несколько дескрипторов.
# И если развивать задачу, то можно сделать класс Предмет, экземпляры которого будут храниться в классе Студент.
# Получится более логично и можно реализовать взаимодействие объектов.
# Тогда уж точно нужно несколько дескрипторов.
# Взять на заметку

if __name__ == '__main__':
    filename = 'lessons.csv'
    lessons = ['Математика', 'Программирование', 'Философия']
    csv_write(filename, lessons)
    student = Student('Иванов', 'Иван', 'Иванович', filename)
    # student = Student('петров', 'Петр', 'Петрович', filename)

    # print(f'Сначала {student.diary = }')
    student.set_grade('Философия', 4)
    student.set_test('Философия', 100)
    student.set_test('Философия', 70)
    student.set_grade('Математика', 3)
    student.set_test('Математика', 70)
    student.set_test('Математика', 50)
    student.set_grade('Программирование', 5)
    student.set_test('Программирование', 100)
    student.set_test('Программирование', 95)
    # student.set_grade('Биология', 5)
    # print(f'Потом {student.diary = }')
    print(f'Средний балл студента {student} по тестам для каждого предмета:\n{student.get_avg_lesson_tests()}')
    print(f'Средний балл студента {student} по оценкам всех предметов вместе взятых: {student.get_avg_lessons()}')
