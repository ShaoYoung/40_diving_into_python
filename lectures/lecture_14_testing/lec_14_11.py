# Основы тестирования
# Задача

import unittest


# from main import func

# мой вариант решения. вывод первого чётного значения или не первого
# def func(my_dict, first = True):
#     if first:
#         count = False
#         for value in my_dict.values():
#             if not value % 2:
#                 if count:
#                     return value
#                 count = not count
#     else:
#         for value in my_dict.values():
#             if not value % 2:
#                 return value

# вариант решения на лекции. вывод первого значения словаря, ключи которого отсортированы по алфавиту, или последнего
def func(my_dict, first = True):
    keys = sorted(my_dict)
    if first:
        return my_dict[keys[0]]
    else:
        return my_dict[keys[-1]]

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

    def test_step_1(self):
        self.assertEqual(func(self.data), 4)

    def test_step_2(self):
        self.assertEqual(func(self.data, first=False), 2)


if __name__ == '__main__':
    unittest.main()
