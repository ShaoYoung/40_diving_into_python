# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUM_OF_ATTEMPTS = 10

number = randint(LOWER_LIMIT, UPPER_LIMIT)

attempt = 0
print(f'Программа загадывает число от {LOWER_LIMIT} до {UPPER_LIMIT}. Необходимо угадать число за {NUM_OF_ATTEMPTS} попыток.')
while attempt < NUM_OF_ATTEMPTS:
    attempt += 1
    user_number = int(input(f'Попытка номер {attempt}. Введите число: '))
    if user_number < number:
        print('Меньше')
    elif user_number > number:
        print('Больше')
    else:
        print(f'Вы отгадали с {attempt} попытки!')
        break
else:
    print(f'Вы использовали все {attempt} попыток и не отгадали число. Было загадано число {number}. Вы проиграли.')