# Урок 15. Обзор стандартной библиотеки Python
# Модуль datetime
# Задача

from datetime import datetime, timedelta

d = datetime.now()
td = timedelta(hours=1)
for i in range(24 * 7):
    if d.weekday() == 6:
        break
    else:
        d = d + td

# количество часов от текущей даты и времени до воскресенья
print(i)
