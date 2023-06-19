# ✔ Создайте функцию-генератор чисел Фибоначчи (см. Википедию).

QUANTITY = 20


def fibonacci(quantity: int) -> iter:
    '''
    Генератор чисел Фибоначчи. Принимает количество чисел Фибоначчи, которое необходимо сгенерировать
    :param quantity: int
    :return: iter
    '''
    a, b = 0, 1
    if quantity:
        yield a
    if quantity > 1:
        yield b
    count = 2
    while count < quantity:
        yield a + b
        count += 1
        a, b = b, a + b


print(*fibonacci(QUANTITY))
