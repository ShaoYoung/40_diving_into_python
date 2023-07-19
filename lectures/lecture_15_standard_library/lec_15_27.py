# Урок 15. Обзор стандартной библиотеки Python
# Модуль argparse
# action
# Параметр action принимает одно из определённых строковых значений и срабатывает при наличии в строке вызова скрипта соответствующего параметра.
# ● store_const — передаёт в args ключ со значением из параметра const
# ● store_true или store_false — сохраняет в ключе истину или ложь
# ● append — ищет несколько появлений ключа и собирает все значения после
# него в список
# ● append_const — добавляет значение из ключа в список, если ключ вызван.
# ○ параметр dest переопределяет имя ключа в Namespace на своё. В результате несколько разных ключей при вызове скрипта имеют одно
# имя при оценке результата.

import argparse

parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()
print(args)

"""
python lec_15_27.py -x -y -z 42 -z 73 -i -f -s
python lec_15_27.py -h
"""
