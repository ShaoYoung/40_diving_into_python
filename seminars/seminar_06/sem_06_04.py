# Задание 4.
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def enigma(question, variants, attempts):
    for i in range(1, attempts + 1):
        answer = input(f'Отгадайте загадку, попытка {i}: {question}: ').strip().lower()
        if answer in variants:
            return (i)
    return 0

__all__ = ['enigma']

if __name__ == '__main__':
    question = 'Зимой и летом одним цветом'
    variants = ['ель', 'ёлка', 'елка']
    attempts = 4
    print(enigma(question, variants, attempts))
