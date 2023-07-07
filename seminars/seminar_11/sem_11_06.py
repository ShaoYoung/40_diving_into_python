# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

from sem_11_05 import Rectangle


class SuperRectangle(Rectangle):
    '''
    Класс SuperRectangle с возможностью сравнения по площади
    '''
    def __init__(self, *args):
        super().__init__(*args)

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __ne__(self, other):
        return self.get_square() != other.get_square()

    def __gt__(self, other):
        return self.get_square() > other.get_square()

    def __ge__(self, other):
        # print('__ge__')
        return other.get_square() >= self.get_square()

    def __lt__(self, other):
        return self.get_square() < other.get_square()

    def __le__(self, other):
        # print('__le__')
        return other.get_square() <= self.get_square()

    def __str__(self):
        return 'Класс SuperRectangle с возможностью сравнения по площади'


if __name__ == '__main__':
    rec_1 = SuperRectangle(4)
    rec_2 = SuperRectangle(3)
    print(f'Площадь {rec_1.get_square() = }')
    print(f'Площадь {rec_2.get_square() = }')
    print(f'{rec_1 == rec_2 = }')
    print(f'{rec_1 != rec_2 = }')
    print(f'{rec_1 > rec_2 = }')
    print(f'{rec_1 <= rec_2 = }')
    print(f'{rec_1 < rec_2 = }')
    print(f'{rec_1 >= rec_2 = }')
    print(rec_1)
