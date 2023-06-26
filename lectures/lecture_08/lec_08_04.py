# Сериализация
# Формат CSV
# Запись CSV

import csv

with (
    open('user_tab.csv', 'r', newline='') as f_read,
    open('user_tab_new.csv', 'w', newline='') as f_write
    ):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line.append('===')
            all_data.append(line)
    print(all_data)
    csv_write.writerows(all_data)


