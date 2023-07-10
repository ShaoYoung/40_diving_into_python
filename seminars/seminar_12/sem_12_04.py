# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# 📌 Используйте декораторы свойств.

class Rectangle:
    '''
    Класс Rectangle. Периметр, площадь, сложение и вычитание прямоугольников.
    '''
    __slots__ = "_length", "_width"

    def __init__(self, *args):
        if len(args) == 1:
            self._length = args[0]
            self._width = self._length
        else:
            self._length, self._width = args

    def get_perimeter(self):
        return self._length * 2 + self._width * 2

    def get_square(self):
        return self._length * self._width

    def get_perimeters(self, other):
        return self._length * 2 + self._width * 2, other.length * 2 + other.width * 2

    def __add__(self, other):
        sum_perimeters = sum(self.get_perimeters(other))
        print(sum_perimeters)
        min_size = min(self._width, self._length, other.width, other.length)
        two_size = (sum_perimeters - min_size * 2) / 2
        return Rectangle(min_size, two_size)

    def __sub__(self, other):
        p_1, p_2 = self.get_perimeters(other)
        sub_perimeters = abs(p_1 - p_2)
        size = sub_perimeters / 4
        return Rectangle(size)

    def __str__(self):
        return 'Класс Rectangle. Периметр, площадь, сложение и вычитание прямоугольников.'

    def __repr__(self):
        return f'Rectangle({self._length}, {self._width})'

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Недопустимое отрицательное значение!")
        else:
            self._length = value

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Недопустимое отрицательное значение!")
        else:
            self._width = value


if __name__ == '__main__':
    rec_1 = Rectangle(5)
    rec_1.length = 6
    print(f'{rec_1.length = }')
    rec_1.width = -6
    print(f'{rec_1.width = }')
