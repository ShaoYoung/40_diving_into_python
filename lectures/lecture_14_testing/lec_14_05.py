# Основы тестирования
# unittest

import unittest


class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(2 * 2, 5, msg='Видимо и в этой вселенной не работает :-(')


if __name__ == '__main__':
    # verbosity=1 - стандартный вывод, verbosity=2 (или любое число, отличное от 1) - подробный вывод о результате работы теста
    unittest.main(verbosity=2)
