# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def make_dict(**kwargs):
    '''
    Принимает на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если
    ключ не хешируем, используется его строковое представление.
    :param kwargs:dict
    :return:dict
    '''
    my_dict = {}
    # for item in kwargs:
    #     try:
    #         my_dict[kwargs[item]] = item
    #     except:
    #         my_dict[str(kwargs[item])] = item

    #     # Тут можно обойтись без обратки исключений.
    #     # Используйте функцию dir чтобы вернуть список атрибутов и методов.
    #     # После проверьте имеется ли там элемент __hash__.
    #     # Скорее всего этот элемент будет в любом случае.
    #     # Функция hash под капотом вызывает именно этот метод, однако он будет прописан только у хэшируемых объектов,
    #     # а у нехэшируемых этого метода нет, но есть одноименный атрибут, который имеет значение None.
    #     # Попробуйте использовать эту информацию.
    for key, value in kwargs.items():
        if value.__hash__:
            my_dict[value] = key
        else:
            my_dict[str(value)] = key

    print(kwargs)
    return my_dict


print(make_dict(param_1=1, param_2='string', param_3=[1, 2, 3], param_4={1, 2, 3}))

# b=[1,2]
# dir(a)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# dir(b)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# a.__hash__
# <method-wrapper '__hash__' of int object at 0x00007FF960A4D328>
# b.__hash__