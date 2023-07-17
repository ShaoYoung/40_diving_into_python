# Задание №6
# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

import pytest

# TODO как прописать путь к проекту ?

import sys
sys.path.append('..\\seminar_13')
from seminars.seminar_13.sem_13_05 import Project
# from sem_13_05 import Project
# from ..seminar_13.sem_13_05 import Project


def test_1():
    filename = '..\\seminar_13\\users.json'
    assert isinstance(Project.load(filename), Project), 'Something is not OK'


# def test_2():
#     pass
#
#
# def test_3():
#     pass
#
#
# def test_4():
#     pass
#
#
# def test_5():
#     pass
#
#
# def test_6():
#     pass
#
#
# def test_7():
#     pass


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
