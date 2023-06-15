# ✔ Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
# Добавить логирование в файл. М.б. через декораторы.

# Задание №6 (семинар 2)
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

from datetime import datetime

# Стартовая сумма
START_SUM = 0
# Сумма, после которой начинается вычитание налога на богатство
RICHES = 5_000_000
# Налог на богатство (%)
RICHES_TAX = 10
# Количество операций, при достижении которого начисляются 3%
COUNT_OPERATIONS = 3
# процент
PERCENT_THIRD_OP = 0.03
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
def refill(account, count, log_list):
    money = input('Введите сумму пополнения, кратную 50 у.е.: ')
    money = int(money) if money.isdigit() else -1
    if money % MULTIPLICITY == 0:
        count, koeff = third_operation(count)
        third_percent_sum = 0
        third_percent_text = ''
        if koeff != 1:
            third_percent_sum = (account + money) * koeff
            third_percent_text = f' начислен % за каждую третью операцию {third_percent_sum},'
        account = account + money + third_percent_sum
        log_list.append(f'refill. Сумма пополнения = {money},{third_percent_text} на счёте {account}.')
        log(log_list[-1])
    else:
        print('Не корректный ввод, повторите.')
    print(f'На вашем счете {round(account, 2)} у.е.')
    return account, count


# Снятие денег
def withdraw_money(account, count, log_list):
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
                third_percent_sum = 0
                third_percent_text = ''
                if koeff != 1:
                    third_percent_sum = (account - money - commission) * koeff
                    third_percent_text = f' начислен % за каждую третью операцию {third_percent_sum},'
                account = account - money - commission + third_percent_sum
                log_list.append(
                    f'withdraw_money. Сумма снятия = {money}, комиссия = {commission},{third_percent_text} на счёте {account}.')
                log(log_list[-1])
    else:
        print('Не корректный ввод, повторите.')
    print(f'На вашем счете {round(account, 2)} у.е.')
    return account, count


# Логирование
def log(log_list_last_record):
    filename = 'bank.log'
    with open(filename, 'a', encoding='utf-8') as log_file:
        log_file.write(f'\n{datetime.now().strftime("%Y %B %d. %H:%M:%S")} -> {str(log_list_last_record)}')


# проверка на богатство
def check_rich(account, log_list):
    if account > RICHES:
        # сумма налога
        tax = account * RICHES_TAX / 100
        account -= tax
        log_list.append(f'check_rich. Удержан налог на богатство = {tax}, на счёте {account}.')
        log(log_list[-1])
    return account


account = START_SUM
log_list = []
count = 0
while True:
    choice = input('Выберите действие (1-пополнить, 2-снять, 3-выйти): ')
    # проверка на богатство после выбора пользователем любого действия
    account = check_rich(account, log_list)
    match choice:
        case '1':
            account, count = refill(account, count, log_list)
        case '2':
            account, count = withdraw_money(account, count, log_list)
        case '3':
            print(f'На вашем счете {round(account, 2)} у.е.')
            break
        case _:
            print('Не корректный ввод. Повторите.')
