# Декораторы

# определение функции-декоратора
def check(input_func):
    def wrapper(name):
        print('### before ###')
        if name == 'qwerty':
            name = f'Привет, {name}'
        else:
            name = f'Ты {name}, я тебя не знаю'
        result = input_func(name)
        return result + '__________'
        print('### after ###')

    return wrapper


@check
def wellcome(name):
    print(name)
    return '123'


if __name__ == '__main__':
    name = 'qwerty'
    print(wellcome(name))
