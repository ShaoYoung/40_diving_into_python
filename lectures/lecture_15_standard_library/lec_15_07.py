# Урок 15. Обзор стандартной библиотеки Python
# Модуль datetime

from datetime import time, date, datetime

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
t_1 = time(hour=2)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0, microsecond=24)
print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{t_1 = }\t-\t{t_1}')
print(f'{dt = }\t-\t{dt}')
