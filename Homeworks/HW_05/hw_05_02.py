# ✔ Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии.

names = ['Петя', 'Вася', 'Маша', 'Люся']
salaries = [100_000, 150_000, 200_000, 250_025]
premiums = ['10.25%', '15.5%', '5.0%', '5.3%']

# statement = {item[0]: round(item[1] * item[2], 2) for item in
#              zip(names, salaries, map(lambda string: float(string[:-1]) / 100, premiums))}

# можно гораздо проще
statement = {name: round(salary * float(premium[:-1]) / 100, 2) for name, salary, premium in
             zip(names, salaries, premiums)}

print(statement)
