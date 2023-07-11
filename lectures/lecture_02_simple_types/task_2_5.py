# строки

text = 'Привет, ' 'как дела?'
print(text)

long_text = '12344132' \
            '123123123'
print(long_text)

text = 'fsaf'\
    'sdgf'\
    'reger'
print(text)

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())