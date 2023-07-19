Документация к модулю getdict
===
**Функция - аналог get для словаря:**

*Возвращает значение по ключу словаря*
*Помимо самого словаря функция принимает ключ и значение по умолчанию*
*При обращении к несуществующему ключу функция должна возвращает дефолтное значение*

Для работы с функцией импортируйте её в свой код.

    >>> from getdict import get_dict

Теперь можно создавать словарь, передавать его в функцию и получать значение по ключу

    >>> my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    >>> key = 1
    >>> default = 'inf'
    >>> print(get_dict(my_dict, key, default))
    one

Если передать несуществующий ключ словаря, то вернётся значение default

    >>> print(get_dict(my_dict, 6, default))
    Ключ 6 в словаре {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'} не обнаружен! Возвращаю дефолтное значение:
    inf

Если передать словарь, ключи которого будут изменяемого типа, то возникнет ошибка

    >>> print(get_dict({[1,2]: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}, [1,2], default))
    Traceback (most recent call last):
    ...
    TypeError: unhashable type: 'list'

*Приятного использования модуля getdict*
