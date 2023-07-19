# Урок 15. Обзор стандартной библиотеки Python
# Модуль logging
# Задача

import logging

logging.basicConfig(filename="log/log.log", encoding='utf-8',
                    format='{asctime} {levelname} {funcName}->{lineno}: {msg}', style='{', level=logging.WARNING)
