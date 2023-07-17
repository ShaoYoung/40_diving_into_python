# pytest

import pytest
from matrix import Matrix


# фикстура m_1
@pytest.fixture
def m_1():
    return Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])


# фикстура m_2
@pytest.fixture
def m_2():
    return Matrix([[1, 1, 1], [2, 2, 2], [0, 0, 0]])


# фикстура m_3
@pytest.fixture
def m_3():
    return Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])


# фикстура m_4
@pytest.fixture
def m_4():
    return Matrix([[1, 1, 1], [2, 2, 2]])


# используем фикстуры m_1 и m_2
def test_not_equal(m_1, m_2):
    assert m_1 != m_2, 'Матрицы оказались равны'


# используем фикстуры m_1 и m_3
def test_equal(m_1, m_3):
    assert m_1 == m_3, 'Матрицы оказались не равны'


# используем фикстуры m_1 и m_4
def test_sum_false(m_1, m_4, capfd):
    # capfd - захват файлового дескриптора. Фикстура, перехватывающая поток вывода и возвращающая соответствующую информацию
    m_1 + m_4
    captured = capfd.readouterr()
    assert captured.out == f'Матрица\n{m_1} и матрица\n{m_4} имеют разные размерности. Сложение невозможно!\n'


# используем фикстуры m_2 и m_3
def test_mul(m_2, m_3, capfd):
    print(m_2 * m_3)
    captured = capfd.readouterr()
    assert captured.out == '6 6 6\n12 12 12\n0 0 0\n'


if __name__ == '__main__':
    pytest.main(['-v'])
