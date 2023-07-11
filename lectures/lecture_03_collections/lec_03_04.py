# строки. форматирование
name = 'Alex'
age = 12

#  1. Не использовать
text = 'Name %s, age %d' % (name, age)
print(text)

# 2. Редко
text = 'Name {}, age {} '.format(name, age)
print(text)

# 3. Использовать
text = f'Name {name}, age {age}'
print(text)

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')

data = [123456,4534543,5462,1]
for item in data:
    print(f'{item:>10}')    # отводится место 10 символов, выравнивание по правому краю
    print(f'{item:<10}')    # отводится место 10 символов, выравнивание по левому краю
    print(f'{item:^10}')    # отводится место 10 символов, выравнивание по центру

num = 2 * pi * data[1]
print(f'{num = :_}')
print(f'{num = }')




