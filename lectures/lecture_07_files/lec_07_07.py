# Файлы и файловая система

import os
from pathlib import Path

# cwd - current work directory
print(os.getcwd())
print(Path.cwd())

# на одну директорию выше
os.chdir('..')
print(os.getcwd())
print(Path.cwd())

# на две директории выше
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())

os.chdir('C:\\')
print(Path.cwd())




