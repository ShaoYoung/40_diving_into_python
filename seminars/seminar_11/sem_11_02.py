# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра

class Archive:
    '''Класс Archive'''
    list_number = []
    list_string = []

    def __init__(self, number, string):
        self.number = number
        self.string = string
        self.list_number.append(number)
        self.list_string.append(string)

    def __str__(self):
        return f'Экземпляр класса {Archive.__name__}. Значения "{self.number} {self.list_number}"'

    def __repr__(self):
        return f'Archive({self.number}, {self.string})'


if __name__ == '__main__':
    a_1 = Archive(1, 'one')
    print(f'{a_1.list_number}')
    print(f'{a_1.list_string}')

    a_2 = Archive(2, 'two')
    print(f'{a_2.list_number}')
    print(f'{a_2.list_string}')

    a_3 = Archive(3, 'three')
    print(f'{Archive.list_number}')
    print(f'{Archive.list_string}')

    # print(help(Archive))
    print(a_1)
    print(f'{a_1 = }')