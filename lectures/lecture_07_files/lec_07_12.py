# Файлы и файловая система

import os
from pathlib import Path
import shutil

# копирование

shutil.copy('data.txt', 'dir')
shutil.copy2('data.txt', 'dir/one_more.txt')
shutil.copytree('dir', 'one_more_dir')


# удаление
shutil.rmtree('one_more_dir')

os.remove('dir/new_name.py')
Path('dir/one_more.txt').unlink()


