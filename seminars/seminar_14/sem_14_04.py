# Задание №4
# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest
from sem_14_01 import clean_text


def test_1():
    assert clean_text('python') == 'python', 'Something is not OK'


def test_2():
    assert clean_text('Python') == 'python', 'Something is not OK'


def test_3():
    assert clean_text('python, but not java') == 'python but not java', 'Something is not OK'


def test_4():
    assert clean_text('python - это не питон') == 'python    ', 'Something is not OK'


def test_5():
    assert clean_text('"Python" - это не "Питон"') == 'python    ', 'Something is not OK'


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])
