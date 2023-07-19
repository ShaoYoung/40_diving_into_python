# unittest

import unittest
from getdict import get_dict


class TestGetDict(unittest.TestCase):
    # создаём две матрицы перед каждым тестом
    def setUp(self) -> None:
        self.dict_1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
        self.dict_2 = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}
        # print('Выполнил setUp')  # Только для демонстрации работы метода

    # получение значения по существующему ключу
    def test_get(self):
        # ожидаем 'two'
        self.assertEqual(get_dict(self.dict_1, 2, 'inf'), 'two')

    # получение значения по несуществующему ключу
    def test_get_wrong_key(self):
        # ожидаем 'inf'
        self.assertEqual(get_dict(self.dict_2, 2, 'inf'), 'inf')


if __name__ == '__main__':
    unittest.main(verbosity=2)
