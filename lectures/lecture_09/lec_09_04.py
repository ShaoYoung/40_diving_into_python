# Декораторы

def add_one_str(a):
    text = ''
    def add_two_str(b):
        nonlocal text
        text += ', ' + b
        return a + text
    return add_two_str


if __name__ == '__main__':
    hello = add_one_str('Hello')
    bye = add_one_str('Good bye')

    print(hello('Alex'))
    print(hello('Karina'))
    print(bye('Alina'))
    print(hello('John'))
    print(bye('Neo'))

