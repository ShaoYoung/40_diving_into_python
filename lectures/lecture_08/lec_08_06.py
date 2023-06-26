# Сериализация
# Формат CSV
# Запись в CSV из словаря

import csv

my_dict = {
    'Name': 'Alex',
    'Sex': 'M',
    'Age': '41',
    'Height': '74',
    'Weight': '170',
    'Office': 'None'
}

with open('user_6.csv', 'w', newline='') as f:
    csv_write = csv.DictWriter(f, fieldnames=["Name", "Sex", "Age", "Height", "Weight", "Office"])
    csv_write.writeheader()
    csv_write.writerow(my_dict)


