# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# Стартовая сумма
START_SUM = 0
# Сумма, после которой начинается вычитание налога на богатство
RICHES = 5_000_000
# Налог на богатство (1 - 0.1)
RICHES_TAX = 0.9
# Количество операций, при достижении которого начисляются 3%
COUNT_OPERATIONS = 3
# процент
PERCENT_THIRD_OP = 1.03
# кратность пополнения / снятия
MULTIPLICITY = 50
# Комиссии
PERCENT_COMISSION = 0.015
MIN_COMISSION = 30
MAX_COMISSION = 600

# Проверка на третью операцию
def third_operation(count):
    count += 1
    if count < COUNT_OPERATIONS:
        koeff = 1
    else:
        count = 0
        koeff = PERCENT_THIRD_OP
    return count, koeff

# Пополнение счёта
def refill(account, count):
    money = input('Введите сумму пополнения, кратную 50 у.е.: ')
    money = int(money) if money.isdigit() else -1
    if money % MULTIPLICITY == 0:
        count, koeff = third_operation(count)
        account = (account + money) * koeff
    else:
        print('Не корректный ввод, повторите.')
    print(f'На вашем счете {round(account, 2)} у.е.')
    return account, count

# Снятие денег
def withdraw_money(account, count):
    money = input('Введите сумму снятия, кратную 50 у.е.: ')
    if money.isdigit():
        money = int(money)
        if money % MULTIPLICITY == 0:
            count, koeff = third_operation(count)
            commission = money * PERCENT_COMISSION
            if commission < MIN_COMISSION:
                commission = MIN_COMISSION
            elif commission > MAX_COMISSION:
                commission = MAX_COMISSION
            if money + commission > account:
                print(f'Недостаточно для снятия {money} у.е.')
            else:
                account = (account - money - commission) * koeff
    else:
        print('Не корректный ввод, повторите.')
    print(f'На вашем счете {round(account, 2)} у.е.')
    return account, count


account = START_SUM
count = 0
while True:
    choice = input('Выберите действие (1-пополнить, 2-снять, 3-выйти): ')
    account = account * RICHES_TAX if account > RICHES else account
    match choice:
        case '1':
            account, count = refill(account, count)
        case '2':
            account, count = withdraw_money(account, count)
        case '3':
            print(f'На вашем счете {round(account, 2)} у.е.')
            break
        case _:
            print('Не корректный ввод. Повторите.')
