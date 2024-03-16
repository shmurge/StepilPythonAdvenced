# Напишите программу, которая транспонирует квадратную матрицу.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

# Формат выходных данных
# Программа должна вывести транспонированную матрицу.

# Примечание 1. Транспонированная матрица — матрица, полученная из исходной матрицы заменой строк на столбцы.

# Примечание 2. Задачу можно решить без использования вспомогательного списка.

def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


def print_transposed_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for c in range(cols):
        for r in range(rows):
            print(str(matrix[r][c]), end=' ')
        print()


n = int(input())
mat_1 = create_matrix(n)
print_transposed_matrix(mat_1)

