# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания. Используйте импорт класса в новый файл.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа, вычисляемый как остаток от деления суммы цифр id на семь

from sem_10_03 import Human
from random import randrange


class Employee(Human):
    MAGIC_KEY = 7
    NUM_ID = 6

    def __init__(self, name, second_name, surname, age, sex):
        self.id_employee = randrange(10 ** (self.NUM_ID - 1), 10 ** (self.NUM_ID))
        # print(f'{self.id_employee = }')
        self.level = sum(map(int, str(self.id_employee))) % self.MAGIC_KEY
        # print(f'{self.level = }')
        super().__init__(name, second_name, surname, age, sex)

    def to_string(self):
        return f'{self.surname} {self.name} {self.second_name} {self.get_age()} {self.sex} {self.id_employee} {self.level}'


if __name__ == '__main__':
    employee_1 = Employee('Иван', 'Иванович', 'Иванов', 30, True)
    print(employee_1.to_string())
