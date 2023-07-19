# Урок 15. Обзор стандартной библиотеки Python
# Модуль logging

import logging
from other import log_all
# уровень логирования - WARNING (отсеиваются менее значимые уровни)
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
