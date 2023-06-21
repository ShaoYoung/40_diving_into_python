# Файлы и файловая система

import os
from pathlib import Path

# перенос

os.replace('bin_1.data', os.path.join(os.getcwd(), 'dir', 'new_name.py'))

old_file = Path('data_1.txt')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)


