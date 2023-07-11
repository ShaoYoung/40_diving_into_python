# Сериализация
# Формат CSV
# Чтение CSV в словарь

import csv

with open('user.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["Name", "Sex", "Age", "Height", "Weight", "Office"], restkey='weight', restval='None')
    for line in csv_file:
        print(f'{line = }')


