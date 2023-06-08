# Байты. Bytes, bytearray>

# Получение байт из строки
text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))

# Получение байт из форматированной строки
# неизменяемая последовательность
x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
# изменяемая последовательность
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x=},\n{y=}')

