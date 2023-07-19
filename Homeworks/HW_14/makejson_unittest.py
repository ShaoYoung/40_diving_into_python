# unittest

import unittest
import json
from makejson import make_json


class TestMakeJSON(unittest.TestCase):
    # создаём две матрицы перед каждым тестом
    def setUp(self) -> str:
        self.filename = 'file_3.txt'
        with open(self.filename, 'w', encoding='utf-8') as f_1:
            line = 'asdfg 333'
            f_1.write(line)
        return self.filename

    # файл не найден
    def test_file_not_found(self):
        # ожидаем FileNotFoundError
        filename = 'badfile.txt'
        with self.assertRaises(FileNotFoundError):
            make_json(filename)

    def test_key_istitle(self):
        make_json(self.filename)
        with open('output.json', 'r', encoding='utf-8') as f_json:
            dict_1 = json.load(f_json)
            for key, value in dict_1.items():
                self.assertTrue(key.istitle(), msg='Ключ не начинается с большой буквы')

    def test_isinstance(self):
        make_json(self.filename)
        with open('output.json', 'r', encoding='utf-8') as f_json:
            dict_1 = json.load(f_json)
            self.assertIsInstance(dict_1, dict)


if __name__ == '__main__':
    unittest.main(verbosity=2)
