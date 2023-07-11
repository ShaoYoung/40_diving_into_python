# Файлы и файловая система

import os
from pathlib import Path

# переименование
# туда
os.rename('data.bin', 'new_data.bin')

# обратно
p = Path('new_data.bin')
p.rename('data.bin')

# более короткая запись
Path('new_data.txt').rename('data_1.txt')


