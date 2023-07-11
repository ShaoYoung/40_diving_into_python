# Декораторы

def add_one_str(a):
    def add_two_str(b):
        return a + ' ' + b
    return add_two_str


if __name__ == '__main__':
    res = add_one_str('Hello')('world')
    # res = add_one_str('Hello')
    print(res)

