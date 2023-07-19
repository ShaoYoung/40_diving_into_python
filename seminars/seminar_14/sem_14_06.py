# Задание №6
# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.

import pytest
import sys

sys.path.append('..\\seminar_13')
from sem_13_05 import Project
from sem_13_03 import AccessException, LevelException
from sem_13_04 import User


# from seminars.seminar_13.sem_13_05 import Project
# from sem_13_05 import Project
# from ..seminar_13.sem_13_05 import Project


@pytest.fixture
def project_1():
    filename = '..\\seminar_13\\users.json'
    return Project.load(filename)


# создание экземпляра класса Project
def test_create(project_1):
    assert isinstance(project_1, Project), 'Something is not OK'


# логин с ошибкой доступа
def test_login_ban(project_1):
    with pytest.raises(AccessException):
        project_1.login('777', 'qwerty')


# разрешённый логин
def test_login(project_1):
    project_1.login('006', 'Люся')
    assert User('006', 'Люся') in project_1.users and project_1.admin.name == 'Люся', 'User did not login'


# добавление пользователя без администратора в проекте
def test_add_user(project_1):
    with pytest.raises(AttributeError):
        project_1.add_user('777', 'qwerty', 0)


# удаление пользователя из проекта
def test_del_user(project_1):
    user_del = User('010', 'Мустафа', '7')
    project_1.del_user(user_del)
    assert user_del not in project_1.users, 'User did not delete'


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
