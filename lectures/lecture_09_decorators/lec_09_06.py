# Декораторы

import random
from typing import Callable


# декоратор кэширования (словарь)
def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


if __name__ == '__main__':
    print(f'{rnd(1, 10) = }')
    print(f'{rnd(1, 10) = }')
    print(f'{rnd(1, 10) = }')
