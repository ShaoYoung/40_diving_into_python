# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

# друзья и вещи
friends = {
    'Вася': ('спички', 'вода', 'нож', 'топор', 'палатка', 'термос'),
    'Петя': ('спички', 'вода', 'нож', 'еда', 'лодка', 'термос'),
    'Гена': ('спички', 'вода', 'нож', 'посуда', 'топор', 'термос'),
    'Ваня': ('карты', 'шашки', 'шахматы', 'топор', 'спички'),
}

# решение первой части задачи с использованием операций с множествами
friends_keys = list(friends.keys())
all_friends = set(friends.get(friends_keys.pop(0)))

for friend_key in friends_keys:
    all_friends = all_friends.intersection(set(friends[friend_key]))
print(*all_friends, 'взяли все', len(friends), 'друга(зей)')

# TODO Обсудить решение с использованием исключительно множеств на ближайшем семинаре

# решение задачи с использованием словарей
# вещи и у кого они есть. ключ - вещь, значение - список друзей, у кого эта вещь есть
things = {}
for friend in friends:
    for thing in friends[friend]:
        # setdefault - классная штука !!!
        things.setdefault(thing, []).append(friend)
# у всех друзей
all_friends = []
# только у одного друга
one_friend = []
# у всех друзей, кроме одного
one_friend_dont_have = {}
for thing in things.items():
    if len(thing[1]) == len(friends):
        all_friends.append(thing[0])
    elif len(thing[1]) == 1:
        one_friend.append(thing[0])
    elif len(thing[1]) == len(friends) - 1:
        for friend in friends:
            if friend not in thing[1]:
                one_friend_dont_have.update({thing[0]: friend})

print(*all_friends, f'взяли все {len(friends)} друга(зей)')
print(*one_friend, 'есть только у одного друга')
for item in one_friend_dont_have:
    print(f'{item} есть у всех друзей, кроме друга по имени {one_friend_dont_have[item]}')
