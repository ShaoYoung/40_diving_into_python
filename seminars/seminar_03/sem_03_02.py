# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в ВЕРХНЕМ регистре в остальных случаях

user_str = input('Введите что-нибудь: ')
if user_str.isdigit():
    print(int(user_str))
elif ',' in user_str or '.' in user_str:
    if user_str.count(',') == 1 or user_str.count('.') == 1:
        if ',' in user_str:
            user_str.replace(',', '.')
        tmp = user_str
        tmp.replace('.', '')    # нет замены !!!
        if tmp.startswith('-'):
            tmp.replace('-', '')
        if tmp.isdigit():
            print(float(user_str))
else:
    upper = True
    for item in user_str:
        if item.isupper():
            print(user_str.lower())
            upper = False
    if upper:
        print(user_str.upper())




# elif ',' in user_str:
#
# if user_str.


