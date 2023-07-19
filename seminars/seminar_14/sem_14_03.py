# Задание №3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest
from sem_14_01 import clean_text


class TestCleanText(unittest.TestCase):
    def test_1(self):
        self.assertEqual(clean_text('python'), 'python', msg='Something is not OK')

    def test_2(self):
        self.assertEqual(clean_text('Python'), 'python', msg='Something is not OK')

    def test_3(self):
        self.assertEqual(clean_text(': python, but not java!!!: '), ' python but not java ', msg='Something is not OK')

    def test_4(self):
        self.assertEqual(clean_text('python не питон'), 'python  ', msg='Something is not OK')

    def test_5(self):
        self.assertEqual(clean_text('"Python" - это не "Питон"'), 'python    ', msg='Something is not OK')


if __name__ == '__main__':
    unittest.main(verbosity=2)
