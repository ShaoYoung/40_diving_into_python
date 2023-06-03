# Напишите небольшую программу, которая
# запрашивает у пользователя текст.
# Если текст можно привести к целому числу,
# выведите его двоичное, восьмиричное
# и шестнадцатиричное представление.
# А если преобразование к целому невозможно,
# сообщите написан ли текст в ASCII или нет.

user_input = input('Введите текст -> ')

if user_input.isdecimal():
    num = int(user_input)
    print(bin(num))
    print(oct(num))
    print(hex(num))
else:
    if user_input.isascii():
        print(f'Текст {user_input} написан в ASCII')
    else:
        print(f'Текст {user_input} написан не в ASCII')

