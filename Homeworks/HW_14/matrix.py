# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    '''Класс Matrix'''

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        '''вывод на печать'''
        to_string = ''
        for row in self.matrix:
            to_string += ' '.join(map(str, row)) + '\n'
        return to_string[:-1]

    def check_dimensions(self, other):
        '''сравнение размерности матриц'''
        if len(self.matrix) != len(other.matrix):
            return False
        for num_row in range(len(self.matrix)):
            if len(self.matrix[num_row]) != len(other.matrix[num_row]):
                return False
        return True

    def check_len_rowA_len_colB(self, other):
        '''сравнение длины строки матрицы A и длины столбца матрицы B. матрицы прямоугольные'''
        return len(self.matrix[0]) == len(other.matrix)

    def __eq__(self, other):
        '''сравнение матриц'''
        if self.check_dimensions(other):
            for num_row in range(len(self.matrix)):
                for num_col in range(len(self.matrix[num_row])):
                    if self.matrix[num_row][num_col] != other.matrix[num_row][num_col]:
                        return False
            return True
        return False

    def __add__(self, other):
        '''сложение матриц'''
        if self.check_dimensions(other):
            matrix = []
            for num_row in range(len(self.matrix)):
                row = []
                for num_col in range(len(self.matrix[num_row])):
                    row.append(self.matrix[num_row][num_col] + other.matrix[num_row][num_col])
                matrix.append(row)
            return Matrix(matrix)
        print(f'Матрица\n{self} и матрица\n{other} имеют разные размерности. Сложение невозможно!')

    def __mul__(self, other):
        '''Умножение матриц
        Операция умножения двух матриц А и В представляет собой вычисление результирующей матрицы С,
        каждый элемент Cij которой равен сумме произведений элементов в соответствующей строке первой матрицы Aik
        и элементов в столбце второй матрицы Bkj.'''
        if self.check_len_rowA_len_colB(other):
            c = []
            for row_a in self.matrix:
                row_c = []
                for j in range(len(other.matrix[0])):
                    col_b = []
                    for i in range(len(other.matrix)):
                        col_b.append(other.matrix[i][j])
                    #     поэлементно перемножаем два списка и суммируем элементы результирующего
                    row_c.append(sum([x * y for x, y in zip(row_a, col_b)]))
                c.append(row_c)
            return Matrix(c)
        else:
            print(f'Длина строки матрицы\n{self}\nи длина столбца матрицы\n{other}\nотличаются. Умножение невозможно!')


if __name__ == '__main__':
    m_1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    m_2 = Matrix([[1, 1, 1], [2, 2, 2], [0, 0, 0]])
    print(f'Матрица\n{m_1}')
    print(f'Матрица\n{m_2}')
    print(f'Сравнение матриц. {m_1 == m_2 = }')
    print(f'Сложение матриц:\n{m_1 + m_2}')
    print(f'Умножение матриц:\n{m_1 * m_2}')
