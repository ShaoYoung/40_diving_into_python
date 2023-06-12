# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

def make_salary(names, salaries, premiums):
    salary_dict = {}
    for name, salary, premium in zip(names, salaries, premiums):
        salary_dict[name] = salary * float(premium[:-1]) / 100
    return salary_dict


name = ['Петя', 'Вася', 'Маша']
salary = [100_000, 150_000, 200_000]
premium = ['5.25%', '7.5%', '10%']

print(make_salary(name, salary, premium))
