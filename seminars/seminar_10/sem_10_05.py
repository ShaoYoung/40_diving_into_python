# Задание №5
# 📌 Создайте три (или более) отдельных классов животных. Например, рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name):
        self.name = name
        self.length = input(f'Введите длину рыбы {self.name} :')

    def get_specific(self):
        return self.length


class Bird:
    def __init__(self, name):
        self.name = name
        self.flying = bool(input(f'{self.name} летает - 1, не летает - 0: '))

    def get_specific(self):
        return self.flying


class Human:
    def __init__(self, name):
        self.name = name
        self.smoke = bool(input(f'{self.name} курит - 1, не курит - 0: '))

    def get_specific(self):
        return self.smoke


if __name__ == '__main__':
    animal_1 = Fish('Карась')
    print(animal_1.get_specific())

    animal_2 = Bird('Орёл')
    print(animal_2.get_specific())

    animal_3 = Human('Европеоид')
    print(animal_3.get_specific())
