# Основы тестирования
# pytest
# pytest fixture
# Задача

import pytest


# решение квадратного уравнения
def func(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))


def test_1():
    assert func(4) == 0


def test_2():
    assert func(4, -4) == (1, 0)


def test_3():
    assert func(4, -10, -50) == (5, -2.5)


def test_4():
    assert func(1, 1, 1) is None


if __name__ == '__main__':
    pytest.main(['-v'])
