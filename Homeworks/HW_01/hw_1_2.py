# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Для поиска всех простых чисел в заданном диапазоне рекомендуется применять решето Эратосфена
# Но в данной задаче надо проверить на простоту только одно число, поэтому алгоритм будет простой с незначительной оптимизацией
MIN_VALUE = 0
MAX_VALUE = 100000
while True:
    number = int(input(f'Введите число от {MIN_VALUE} до {MAX_VALUE}: '))
    # сделано проще
    if MIN_VALUE <= number <= MAX_VALUE:
        break
    # сделано без else
    print('Не корректный ввод. Попробуйте ещё раз')
if number == 0 or number == 1:
    print(f'Число {number} не является ни простым, ни составным')
elif number % 2 == 0 and number != 2:
    print(f'Число {number} составное')
else:
    check_number = f'Число {number} простое'
    for i in range(3, number // 2 + 1, 2):
        if number % i == 0:
            check_number = f'Число {number} составное'
            # добавлен break для исключения проверки остальных делителей. число уже составное.
            break
    print(check_number)
