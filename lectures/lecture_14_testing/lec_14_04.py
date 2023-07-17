# Основы тестирования
# Задача


def say(text_1, count = 2, text_2 = ' '):
    """
    >>> say('Hello')
    Hello Hello
    >>> say('Hi', 5)
    Hi Hi Hi Hi Hi
    >>> say('cat', 3, '(=^.^=)')
    cat(=^.^=)cat(=^.^=)cat
    """
    print((text_1 + text_2) * (count-1) + text_1)



if __name__ == '__main__':
    import doctest
    # Подробный вывод
    doctest.testmod(verbose=True)

    # say("Hello")
    # say('Hi', 5)
    # say('cat', 3, '(=^.^=)')
