# Задание №5
# 📌 На семинарах по ООП был создан класс прямоугольник, хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_1(self):
        self.assertIsInstance(Rectangle(5), Rectangle)

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
