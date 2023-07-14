# Прямоугольник.

from hw_13_01 import IncorrectSideException

class Rectangle:
    def __init__(self, *args):
        for side in args:
            if side < 0:
                raise IncorrectSideException(side)
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width = args

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def get_square(self):
        return self.length * self.width


if __name__ == '__main__':
    rectangle_1 = Rectangle(1, 2)
    print(f'{rectangle_1.get_perimeter() = }')
    print(f'{rectangle_1.get_square() = }')
    rectangle_2 = Rectangle(-2)
    print(f'{rectangle_2.get_perimeter() = }')
    print(f'{rectangle_2.get_square() = }')
