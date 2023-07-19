# Задача из семинара №11
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длину и ширину.
# 📌 При вычитании не допускайте отрицательных значений.
# Новый прямоугольник: меньшая сторона = const
# Вычитание из большего меньшего (модуль)
class Rectangle:
    '''
    Класс Rectangle. Периметр, площадь, сложение и вычитание прямоугольников.
    '''

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

    def __eq__(self, other):
        return self.get_perimeter() == other.get_perimeter() and self.get_square() == other.get_square()

    def __str__(self):
        return 'Класс Rectangle. Периметр, площадь, сложение и вычитание прямоугольников.'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


if __name__ == '__main__':
    rec_1 = Rectangle(5)
    rec_2 = Rectangle(5, 6)
    sum_rec = rec_1 + rec_2
    print(sum_rec.length, sum_rec.width)
    sub_rec = rec_1 - rec_2
    print(sub_rec.length, sub_rec.width)
    print(rec_1)
    print(f'{rec_1 = }')

    rec = Rectangle(5)
    # rec_3 = Rectangle('q')
    # sum_rec = rec_3 + rec_3
    print(Rectangle(5) == Rectangle(5))
