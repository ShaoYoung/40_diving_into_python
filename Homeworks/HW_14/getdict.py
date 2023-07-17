# Задание №2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.


def get_dict(my_dict, key, default):
    try:
        return my_dict[key]
    except KeyError:
        print(f'Ключ {key} в словаре {my_dict} не обнаружен! Возвращаю дефолтное значение:')
        return default


if __name__ == '__main__':
    my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    key = 6
    default = 'inf'
    print(get_dict(my_dict, key, default))
