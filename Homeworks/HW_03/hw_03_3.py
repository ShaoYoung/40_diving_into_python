# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Верните все возможные варианты комплектации рюкзака.

# Нагуглил модуль itertools. Решил использовать его для поиска всех возможных комбинаций ключей словаря.
from itertools import combinations

things = {
    'топор': 2,
    'палатка': 5,
    'еда': 3,
    'вода': 3,
    'спальник': 2,
    'посуда': 1,
    'термос': 1,
    'одежда': 4,
    'обувь': 2,
    'удочка': 1,
}
MAX_LOAD = 20
can_fit = {}
things_combinations = []
# делаем список всех возможных комбинаций вещей (используя функцию combinations модуля itertools)
# можно собрать вручную при помощи циклов
for i in range(1, len(things) + 1):
    things_combinations += list(combinations(things, i))
# текущая максимальная загрузка
max_load = MAX_LOAD
# проверяем массу каждой комбинации вещей
while True:
    for combination in things_combinations:
        sum_combination = 0
        for item in combination:
            sum_combination += things[item]
        if sum_combination == max_load:
            can_fit.update({combination: sum_combination})
    # если комбинации текущую максимальную загрузку найдены, выходим из цикла
    if can_fit:
        print((f'Варианты загрузки рюкзака на {max_load}:'))
        break
    # уменьшаем предел максимальной загрузки рюкзака
    print(f'Не получается загрузить рюкзак на {max_load}. Пробую загрузить на {max_load - 1}.')
    max_load -= 1
# вывод всех возможных комбинаций вещей и их веса
for i, combination in enumerate(can_fit.items(), 1):
    print(i, *combination)
