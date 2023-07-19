# Урок 15. Обзор стандартной библиотеки Python
# Модуль collections
# namedtuple

from collections import namedtuple
from datetime import datetime

# создаётся класс User
User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
# экземпляр класса
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(f'{type(User)}, {type(u_1)}')
print(u_1.first_name, u_1.birthday.year)
