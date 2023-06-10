# функции
# позиционные и ключевые параметры

def standard_arg(arg):
    return arg


def pos_only_arg(arg, /):
    return arg


def kwd_only_arg(*, arg):
    return arg


def combined_ex(pos_only, /, standard, *, kwg_only):
    return(pos_only, standard, kwg_only)


standard_arg(42)  # позиционное значение
standard_arg(arg=42)  # ключевое значение

pos_only_arg(42)  # всё работает
# pos_only_arg(arg=42)    # ошибка, т.к. должен быть позиционный аргумент. передача ключевых элементов запрещена

# kwd_only_arg(42)    # ошибка, т.к. должен передаваться ключевой аргумент
kwd_only_arg(arg=42)

# combined_ex(1,2,3)      # ошибка
combined_ex(1,2,kwg_only=3)     # нормально
combined_ex(1, standard=2, kwg_only=3)      # нормально
# combined_ex(pos_only=1, standard=2, kwg_only=3)     # ошибка



