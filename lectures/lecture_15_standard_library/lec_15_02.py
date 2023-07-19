# Урок 15. Обзор стандартной библиотеки Python
# Модуль logging

import logging
# logging.NOTSET - логируется всё
logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')


