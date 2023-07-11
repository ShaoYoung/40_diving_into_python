# Сериализация
# Формат CSV
# Чтение CSV

import csv

with open('user.csv', 'r', newline='') as f:
# параметр newline='' для работы с CSV
    csv_file = csv.reader(f)
# csv_file позволяет построчно читать csv файл в список list
    for line in csv_file:
        print(line)
    print(type(line))

print(csv_file)

with open('user_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)

