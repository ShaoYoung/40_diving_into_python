# pytest

import pytest
from getdict import get_dict


# фикстура dict_1
@pytest.fixture
def dict_1():
    return {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


# фикстура dict_2
@pytest.fixture
def dict_2():
    return {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}


# используем фикстуру dict_1
def test_get_value_right_key(dict_1):
    assert get_dict(dict_1, 3, 'inf') == 'three'


# используем фикстуру dict_2
def test_get_value_wrong_key(dict_2):
    assert get_dict(dict_2, 3, 'inf') != 'three'


# используем фикстуру dict_2
def test_show_print(dict_2, capfd):
    # capfd - захват файлового дескриптора. Фикстура, перехватывающая поток вывода и возвращающая соответствующую информацию
    key = 3
    get_dict(dict_2, 3, 'inf')
    captured = capfd.readouterr()
    assert captured.out == f'Ключ {key} в словаре {dict_2} не обнаружен! Возвращаю дефолтное значение:\n'


if __name__ == '__main__':
    pytest.main(['-v'])
