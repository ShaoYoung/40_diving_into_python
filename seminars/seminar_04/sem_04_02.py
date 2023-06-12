# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text = 'Однажды в студёную зимнюю пору я из лесу вышел был сильный мороз'

def unicode(text):
    chr_text = []
    for item in set(text):
        chr_text.append(ord(item))
    chr_text = sorted(chr_text, reverse=True)
    return chr_text


print(unicode(text))


