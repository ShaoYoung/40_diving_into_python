# pytest
import json

import pytest
from makejson import make_json
from random import choices


# фикстура filename_1
@pytest.fixture
def filename_1():
    filename = 'file_1.txt'
    list_numbers = [str(i) for i in range(0,10)]
    list_letters = [chr(i) for i in range(97, 123)]
    with open(filename, 'w', encoding='utf-8') as f_1:
        lines = []
        for _ in range(0,10):
            lines.append(''.join(choices(list_letters, k=5)) + ' ' + ''.join(choices(list_numbers, k=3)) + '\n')
        f_1.writelines(lines)
    return filename

# фикстура filename_2
@pytest.fixture
def filename_2():
    filename = 'file_2.txt'
    with open(filename, 'w', encoding='utf-8') as f_1:
        line = 'qwerty 111'
        f_1.write(line)
    return filename

# используем фикстуру filename_1
def test_filename_1(filename_1):
    make_json(filename_1)
    with open('output.json', 'r', encoding='utf-8') as f_json:
        dict_1 = json.load(f_json)
    assert isinstance(dict_1, dict), 'Это не словарь'

# используем фикстуру filename_2
def test_filename_2(filename_2):
    make_json(filename_2)
    with open('output.json', 'r', encoding='utf-8') as f_json:
        dict_1 = json.load(f_json)
        for key, value in dict_1.items():
            assert key == 'Qwerty', 'Не Qwerty'
            assert value == '111', 'Не 111'

def test_file_not_found():
    filename = 'badfile.txt'
    with pytest.raises(FileNotFoundError):
        make_json(filename)


def test_key_istitle(filename_1):
    make_json(filename_1)
    with open('output.json', 'r', encoding='utf-8') as f_json:
        dict_1 = json.load(f_json)
        for key, value in dict_1.items():
            assert key.istitle(), 'Ключ не начинается с большой буквы'



if __name__ == '__main__':
    pytest.main(['-v'])
