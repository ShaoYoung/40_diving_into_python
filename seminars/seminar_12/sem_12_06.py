# Задание №6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
class Range:
    # Обязательно, для установления связи
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < 0:
            raise ValueError("Недопустимое отрицательное значение!")
        return True


class Rectangle:
    length = Range()
    width = Range()
    '''
    Класс Rectangle. Периметр, площадь, сложение и вычитание прямоугольников.
    '''
    # __slots__ = "_length", "_width"

    def __init__(self, *args):
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width = args

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def get_square(self):
        return self.length * self.width

    def get_perimeters(self, other):
        return self.length * 2 + self.width * 2, other.length * 2 + other.width * 2

    def __add__(self, other):
        sum_perimeters = sum(self.get_perimeters(other))
        print(sum_perimeters)
        min_size = min(self.width, self.length, other.width, other.length)
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
        return f'Rectangle({self.length}, {self.width})'


if __name__ == '__main__':
    rec_1 = Rectangle(5)
    rec_1.length = 6
    print(f'{rec_1.length = }')
    rec_1.width = 7
    print(f'{rec_1.width = }')
