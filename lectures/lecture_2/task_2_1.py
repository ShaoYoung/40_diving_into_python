
# Изменяемые и неизменяемые типы
user_input = '12345'
print(f'Тип объекта {type(user_input)}')
print(f'Адрес объекта в ОЗУ {id(user_input)}')
print(f'Хеш объекта {hash(user_input)}')

# Аннотация типов
def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res
print(my_func([2, 5.5, 8, 87.89]))
a: int = 45
b: int = 45.5
c: int | float = 56.6



