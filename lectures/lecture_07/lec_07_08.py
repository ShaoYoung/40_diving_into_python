# Файлы и файловая система

import os
from pathlib import Path
import shutil

# # создание новой директории
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()
#
# # создание директорий с несколькими уровнями вложенности
# os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir()  # FileNotFound
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# удаление директорий (пустых)
# os.rmdir('dir')
# Path('some_dir').rmdir()
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()

# удаление директорий с помощью shutil (рекурсивно)
# shutil.rmtree('dir/other_dir')
# shutil.rmtree('some_dir')

# формирование путей
file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')

