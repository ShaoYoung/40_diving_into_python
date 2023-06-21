# Файлы и файловая система

import os
from pathlib import Path

# получение каталогов и файлов текущей директории
print(os.listdir())
p = Path(Path.cwd())
for obj in p.iterdir():
    print(obj)

# определение типа
dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end = '\t')
    print(f'{os.path.isfile(obj) = }', end = '\t')
    print(f'{os.path.islink(obj) = }', end = '\t')
    print(f'{obj = }')

p = Path(Path.cwd())        # p - объект типа windowsPath
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end = '\t')
    print(f'{obj.is_file() = }', end = '\t')
    print(f'{obj.is_symlink() = }', end = '\t')
    print(f'{obj = }')

# рекурсивный вывод содержимого директории
for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
