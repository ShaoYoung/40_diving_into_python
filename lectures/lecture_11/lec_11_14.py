# ООП. Особенности Python.
# Обработка атрибутов

# Получение значения атрибута, __getattribute__
# Дандер __getattribute__ вызывается при любой попытке обращения к атрибутам экземпляра
# class Name:
    # ...
    # def __getattribute__(self, item):
        # ...
        # return object.__getattribute__(self, item)

# Присвоение атрибуту значения, __setattr__
# Дандер __setattr__ срабатывает каждый раз, # когда в коде есть операция присвоения
# class Name:
    # ...
    # def __setattr__(self, key, value):
        # ...
        # return object.__setattr__(self, key, value)

# Обращение к несуществующему атрибуту, __getattr__
# Если свойство отсутствует, в первую очередь вызывается дандер __getattribute__. В случае возврата им ошибки AttributeError
# вызывается метод __getattr__
# class Name:
    # ...
    # def __getattr__(self, item):
        # ...
        # return ...

# Удаление атрибута, __delattr__
# Дандер __delattr__ вызывается при попытке удалить атрибут командой del
# class Name:
    # ...
    # def __delattr__(self, item):
        # ...
        # object.__delattr__(self, item)

# Функции setattr(), getattr() и delattr()
# 💡 setattr(object, name, value)
# аналог object.name = value
# 💡 getattr(object, name[, default])
# аналог object.name or default
# 💡 delattr(object, name)
# аналог del object.name


