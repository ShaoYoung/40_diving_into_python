# ✔ Напишите функцию для транспонирования матрицы

def trans_matrix(matrix):
    '''
    транспонирует матрицу (список списков)
    :param matrix:list(list)
    :return:list(list)
    '''
    trans_mat = []
    # Задаём количество строк транспонированной матрицы
    for i in range(len(matrix[0])):
        trans_mat.append([])
    # транспонируем
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            trans_mat[j].append(matrix[i][j])
    return trans_mat


def trans_matrix_gen(matrix):
    '''
    транспонирует матрицу (список списков). используется генератор list comprehensions
    :param matrix:list(list)
    :return:list(list)
    '''
    trans_mat = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_mat


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]
print(f'Source {matrix = }')
print(f'Transposed matrix = {trans_matrix(matrix)}')
print(f'Transposed matrix_gen = {trans_matrix_gen(matrix)}')
