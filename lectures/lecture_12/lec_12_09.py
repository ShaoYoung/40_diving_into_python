# ООП. Финал.
# Декоратор @property
# Getter

class User:
    def __init__(self, name):
        self._name = name

    # применён декоратор. теперь name воспринимается как название свойства
    @property
    def name(self):
        return self._name


user = User('Стивен')
print(f'{user.name = }')
user.name = 'Славик'  # AttributeError: can't set attribute 'name'
