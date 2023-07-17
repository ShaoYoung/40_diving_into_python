# unittest

import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    # создаём две матрицы перед каждым тестом
    def setUp(self) -> None:
        self.m_1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        self.m_2 = Matrix([[1, 1, 1], [2, 2, 2], [0, 0, 0]])
        print('Выполнил setUp')  # Только для демонстрации работы метода

    # создание экземпляра
    def test_create(self):
        # ожидаем True
        self.assertIsInstance(self.m_1, Matrix, msg='This is not Matrix class')

    # сравнение экземпляров
    def test_equal(self):
        # ожидаем True
        self.assertNotEqual(self.m_1, self.m_2)

    # сравнение размерности экземпляров
    def test_check_dimensions(self):
        # ожидаем True
        self.assertTrue(self.m_1.check_dimensions(self.m_2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
