# Задание №1
# 📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

class Factorial:
    def __init__(self, k):
        self.k = k
        self.list_dict = []

    def __call__(self, *args, **kwargs):
        num = args[0]
        fac = 1
        for i in range(2, num + 1):
            fac *= i
        self.list_dict.append({num: fac})
        if len(self.list_dict) >= self.k:
            self.list_dict = self.list_dict[-self.k:]
        return fac

    def show(self):
        return self.list_dict


if __name__ == '__main__':
    factorial = Factorial(5)
    for i in range(1, 10):
        f = factorial(i)
        print(f)
    print(factorial.show())
