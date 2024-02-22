# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу,
# которая выводит след заданной квадратной матрицы.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — след заданной матрицы.

n = int(input())


def create_sqrt_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = int(matrix[i][j])

    return matrix


def print_matrix_trace(matrix):
    size = len(matrix)
    score = 0
    for r in range(size):
        score += int(matrix[r][r])

    return score


mat_1 = create_sqrt_matrix(n)
trace = print_matrix_trace(mat_1)
print(trace)
