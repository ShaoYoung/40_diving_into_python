# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# * - вывести все успешные расстановки

from itertools import combinations
from random import randint

LENGTH_OF_DESK = 8
NUM_OF_QUEENS = 8
NUM_OF_COMB = 4


def queen_cuts(queens_coord: list | tuple | set) -> bool:
    '''
    Проверяет расстановку 8 ферзей на шахматной доске. Возвращает True, если ферзи не бьют друг друга и False, если хотя бы один бьёт другого
    :param queens_coord: list(list(2)
    :return: bool
    '''
    # print(queens_coord)
    for i in range(0, len(queens_coord)):
        for j in range(i + 1, len(queens_coord)):
            # print(queens_coord[i], queens_coord[j])
            if queens_coord[i][0] == queens_coord[j][0] or queens_coord[i][1] == queens_coord[j][1] or abs(
                    queens_coord[i][0] - queens_coord[j][0]) == abs(queens_coord[i][1] - queens_coord[j][1]):
                return False
    return True


def get_random_desk_combination(length_of_desk: int) -> list:
    '''
    генерирует случайную расстановку ферзей
    :param length_of_desk: int
    :return: list
    '''
    random_desk_combination = set()
    while len(random_desk_combination) <= length_of_desk:
        coord_a, coord_b = randint(1, length_of_desk), randint(1, length_of_desk)
        random_desk_combination.add((coord_a, coord_b))
    return list(random_desk_combination)


def get_num_combinations(num_of_comb: int, length_of_desk) -> set:
    '''
    Возвращает множество случайных num_of_comb комбинаций
    :param num_of_comb: количество комбинаций, которое необходимо найти
    :param length_of_desk: размер шахматной доски
    :return: set
    '''
    num_desk_combinations = set()
    count = 0
    while count < num_of_comb:
        random_desk_combination = get_random_desk_combination(length_of_desk)
        if queen_cuts(random_desk_combination):
            count += 1
            num_desk_combinations.add(random_desk_combination)
            # print(f'{count} комбинация = {random_desk_combination}')
    return num_desk_combinations


def get_all_desk_combination(length_of_desk: int, num_of_queens: int) -> set:
    '''
    Возвращает множество всех комбинаций
    :param length_of_desk: размер шахматной доски
    :param num_of_queens: количество ферзей
    :return: set
    '''
    all_desk_combination = set()
    # генерируем множество возможных положений одного ферзя на доске размером length_of_desk х length_of_desk
    one_queen_desk_combinations = set(
        (i, j) for i in range(1, length_of_desk + 1) for j in range(1, length_of_desk + 1))
    # print(f'one_queen_desk_combinations = {one_queen_desk_combinations}')

    # генерируем итератор всех возможных вариантов расстановки num_of_queens ферзей на доске размером length_of_desk х length_of_desk
    desk_combinations = combinations(one_queen_desk_combinations, num_of_queens)

    count = 0
    # проверяем каждую комбинацию. если проверка пройдена, выводим номер и кортеж пар координат
    for combination in desk_combinations:
        if queen_cuts(combination):
            count += 1
            print(f'{count} = {combination}')
            all_desk_combination.add(combination)
    return all_desk_combination


if __name__ == '__main__':
    # print(f'{NUM_OF_COMB} случайные комбинации, при которых ферзи не бьют друг друга:')
    # print(*get_num_combinations(NUM_OF_COMB, LENGTH_OF_DESK))

    print('Все комбинации, при которых ферзи не бьют друг друга (прийдётся часок подождать):')
    # Нашёл 92 комбинации расстановки ферзей
    print(*get_all_desk_combination(LENGTH_OF_DESK, NUM_OF_QUEENS))
