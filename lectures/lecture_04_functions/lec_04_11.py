# функции

# locals, globals, vars

SIZE = 10


def func(a, b, c):
    x = a + b
    print(locals())
    print(globals())
    z = x + c
    return z


print(globals())
func(1, 2, 3)

print(vars(int))


data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'),globals().items()))
