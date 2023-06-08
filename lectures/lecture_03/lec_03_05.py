# строки. методы

link = 'https://gb.ru/lessons/336288'
urls = link.split('/')
print(urls)

# a, b, c = input('Введите 3 числа через пробел ').split()
# print(a, b, c)
#
# # *_ - упаковать лишнее во временный кортеж _
# a, b, c, *_ = input('Введите 3 числа через пробел ').split()
# print(a, b, c)
# print(_)
# # безопаснее использовать
# lst = input('Введите 3 числа через пробел ').split()

url = '/'.join(urls)
print(url)

text = 'Однажды в студёную зимнюю пору'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))



