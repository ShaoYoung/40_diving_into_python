# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длину и ширину.
# 📌 При вычитании не допускайте отрицательных значений.
# Новый прямоугольник: меньшая сторона = const
# Вычитание из большего меньшее
class Rectangle:
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


if __name__ == '__main__':
    rec_1 = Rectangle(5)
    rec_2 = Rectangle(5, 6)
    sum_rec = rec_1 + rec_2
    print(sum_rec.length, sum_rec.width)
    sub_rec = rec_1 - rec_2
    print(sub_rec.length, sub_rec.width)
