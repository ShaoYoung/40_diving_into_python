# Задание 5.
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

from sem_06_04 import enigma


def game(attempts=5):
    dict_enigma = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'елка'],
        'Кто его раздевает, тот слёзы проливает': ['лук', 'лучок', 'перец'],
    }
    for key, value in dict_enigma.items():
        save_result(key, enigma(key, value, attempts))


def save_result(key, num_of_att):
    _res_dict[key] = num_of_att


def print_res(_res_dict):
    gen = (key + '-' + str(value) + '\n' for key, value in _res_dict.items())
    print(*gen)

# Функций, работающих полноценно и верно за пределами этого модуля, нет
# только при условии последовательного вызова. Можно добавить ещё одну объединяющую функцию.
__all__ = []
_res_dict = {}

if __name__ == '__main__':
    game()
    print_res(_res_dict)

