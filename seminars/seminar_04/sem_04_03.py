# Задание №3
# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением —  его порядковый номер из диапазона, границами которого являются введенные числа.
# Границы диапазона учитывать.
#

string = '56 50'

def convert(string):
    start, end = map(int, string.split())
    our_dict = {}
    if start > end:
        start, end = end, start
    for item in range(start, end + 1):
        our_dict[chr(item)] = item
    return our_dict


print(convert(string))

