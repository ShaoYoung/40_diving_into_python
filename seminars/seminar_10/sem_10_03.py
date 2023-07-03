# Задание 3.
# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Cвойство возраст должно быть недоступно для прямого обращения, но возможность получить текущий возраст должна присутствовать.

class Human:
    def __init__(self, name, second_name, surname, age, sex):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.__age = age
        self.sex = sex

    def birthday(self):
        self.__age += 1
        return self.__age

    def full_name(self):
        return f'{self.surname} {self.name} {self.second_name}'

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    human_1 = Human('Иван', 'Иванович', 'Иванов', 30, True)
    print(f'{human_1.birthday() = }')
    print(f'{human_1.full_name()}')
    print(f'{human_1.get_age()}')
    print(f'{human_1._Human__age}')
