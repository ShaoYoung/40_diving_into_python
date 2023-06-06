# Простые типы
x = int('42')
y = int(3.1415)
z = int('hello', base=30)
print(x, y, z, sep='\n')

# цикл for, если переменная не нужна, а нужны лишь итерации
for _ in range(30):
    pass

# разделители цифр в числе
num = 7_123_456_789_0
print(num)

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)
print(b, o, h)



