# Задание №3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, *args):
        if len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        elif len(args) == 1:
            self.stop = args[0]
            self.start = 1
            self.step = 1
        else:
            self.start, self.stop, self.step, *_ = args
        # print(f'{self.start = }\t{self.stop = }\t{self.step = }')

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            fac = 1
            for i in range(self.start, self.stop + 1, self.step):
                fac *= i
            self.start += self.step
            return fac
        raise StopIteration


if __name__ == '__main__':
    factorial = Factorial(1, 10, 1)
    for i in factorial:
        print(i)
