# Основы тестирования
# сравнение doctest и unittest

import doctest
import unittest
import lec_14_06

def load_tests(loader, tests, ignore):
    # передаём файл с кодом. Тест НЕ ЗАПУСКАЕТСЯ !!!
    tests.addTests(doctest.DocTestSuite(lec_14_06))
    # передаём файл с тестами
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests

if __name__ == '__main__':
    unittest.main()


