# Задание №2
# 📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string
def clean_text(text: str) -> str:
    """
    Delete symbols from text other than A(a) - Z(z) and space. Return string in lower register.
    >>> clean_text('python')
    'python'
    >>> clean_text('Python')
    'python'
    >>> clean_text(': python, but not java!!!: ')
    ' python but not java '
    >>> clean_text('python не питон')
    'python  '
    >>> clean_text('"Python" - это не "Питон"')
    'python    '
    """
    str_chars = string.ascii_letters + ' '
    text = ''.join([item if item in str_chars else '' for item in text]).lower()
    # text = text.lower()
    # av_symbols = [chr(code) for code in range(97, 123)]
    # av_symbols.append(' ')
    # for symbol in text:
    #     if symbol not in av_symbols:
    #         text = text.replace(symbol, '')
    return text


if __name__ == '__main__':
    import doctest
    # Подробный вывод
    doctest.testmod(verbose=True)

