# Урок 15. Обзор стандартной библиотеки Python
# Модуль argparse


import argparse

parser = argparse.ArgumentParser(prog='average', description='My first argument parser', epilog='Returns the arithmetic mean')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')


"""
python lec_15_23.py 42 3.14 73
python lec_15_23.py --help
python lec_15_23.py Hello
"""



