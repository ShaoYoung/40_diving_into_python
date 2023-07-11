# значение по умолчанию
DEFAULT = 42
num = int(input('-> '))
level = num or DEFAULT
print(level)

# значение по умолчанию
name = input('Name -> ')
if name:
    print(name)
else:
    print('anonim')


data = [0,1,2,3,4,5,6,7,8,9]
while data:
    print(data.pop())

