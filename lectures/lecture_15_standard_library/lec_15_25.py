# Урок 15. Обзор стандартной библиотеки Python
# Модуль argparse


import argparse

def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float, nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(args)
    print(quadratic_equations(*args.param))



"""
python lec_15_25.py 2 -12 10
python lec_15_25.py -h
"""
