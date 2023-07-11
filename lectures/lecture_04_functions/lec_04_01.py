# функции
# функции высшего порядка

a = 42
print(type(a), id(a))
print(type(id))

very_bad_programming_style = sum
print(very_bad_programming_style([1, 2, 3]))


# эту конструкцию надо использоватьlec_04_01.py при возможной передаче пустого изменяемого объекта в аргумент функции
def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(new_list)
