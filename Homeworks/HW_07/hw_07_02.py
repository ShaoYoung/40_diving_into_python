# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов <new_name>.
# * При переименовании в конце имени добавляется порядковый номер <position>.
# * принимать в качестве аргумента расширение исходного файла (source_ext).
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла <new_extension>.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extension>


import os


def rename_files(new_name, source_ext, new_ext, folder):
    # переходим в папку
    os.chdir(folder)
    # собираем список (только) файлов
    list_files = filter(lambda file_obj: os.path.isfile(file_obj), os.listdir(folder))
    position = 0
    for file in list_files:
        new_filename = ''
        original_name, ext = file.split('.')
        # если совпало расширение исходного файла
        if ext == source_ext:
            position += 1
            # собираем новое имя
            new_filename += original_name + '_' + new_name + '_' + str(position) + '.' + new_ext
            # print(new_filename)
            os.rename(file, new_filename)


if __name__ == '__main__':
    new_name = '==='
    source_ext = 'jpg'
    new_ext = 'png'
    folder = os.path.join(os.getcwd(), 'folder_02')
    rename_files(new_name, source_ext, new_ext, folder)
