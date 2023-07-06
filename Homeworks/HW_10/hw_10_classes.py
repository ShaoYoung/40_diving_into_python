# Задание №6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    prop = {1: 'Пресноводная',
            2: 'Морская'
            }

    def __init__(self, name, specific):
        super().__init__(name)
        self.spec_op = self.prop[specific]

    def get_specific(self):
        return self.spec_op


class Bird(Animal):
    prop = {1: 'Летает',
            2: 'Не летает'
            }

    def __init__(self, name, specific):
        super().__init__(name)
        self.spec_op = self.prop[specific]

    def get_specific(self):
        return self.spec_op


class Human(Animal):
    prop = {1: 'Курит',
            2: 'Не курит'
            }

    def __init__(self, name, specific):
        super().__init__(name)
        self.spec_op = self.prop[specific]

    def get_specific(self):
        return self.spec_op


if __name__ == '__main__':
    animal_1 = Fish('Карась', 1)
    print(animal_1.get_specific())

    animal_2 = Bird('Орёл', 1)
    print(animal_2.get_specific())

    animal_3 = Human('Европеоид', 1)
    print(animal_3.get_specific())
