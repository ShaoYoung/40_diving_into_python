# Урок 15. Обзор стандартной библиотеки Python
# Модуль collections
# namedtuple

import time
from collections import namedtuple
from datetime import datetime
# default значения формируются не при создании экземпляра класса, а при создании самого класса
# не указывать значения каких-либо функций, к-е могут измениться во времени
User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
time.sleep(7)
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
