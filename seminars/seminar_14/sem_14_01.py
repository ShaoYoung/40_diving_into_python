# Задание №1
# 📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

def clean_text(text: str) -> str:
    text = text.lower()
    av_symbols = [chr(code) for code in range(97, 123)]
    av_symbols.append(' ')
    for symbol in text:
        if symbol not in av_symbols:
            text = text.replace(symbol, '')
    return text


if __name__ == '__main__':
    print(clean_text('Однажды в студёную зимнюю пору...Python is the most popular programming language'))
