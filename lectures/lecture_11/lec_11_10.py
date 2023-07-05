# ООП. Особенности Python.
# Представления экземпляра

class User:

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр класса User c именем "{self.name}"'

    def __repr__(self):
        return f'User({self.name})'

user = User('Вася')
print(user)
print(f'{user}')
print(repr(user))
print(f'{user = }')
# print(collections)
