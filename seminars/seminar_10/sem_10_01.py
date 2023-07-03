# Задание №1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_length(self):
        return 2 * math.pi * self.__radius

    def get_square(self):
        return math.pi * self.__radius ** 2


if __name__ == '__main__':
    circle_1 = Circle(1)
    print(f'{circle_1.get_length() = }')
    print(f'{circle_1.get_square() = }')
