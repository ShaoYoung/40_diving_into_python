# строки
text = 'Hello, world'
print(text[5])
print(text[3:7])
print(text[3:8:2])

new_text = text.replace('l', 'L')
print(text, new_text, sep=' === ')

text.replace('L', 'W')      # text останется неизменной
print(text)

print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))   # -1

print(text[::-1])




