# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
# больших среднего арифметического элементов данной строки.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести n чисел — для каждой строки количество элементов матрицы,
# больших среднего арифметического элементов данной строки.


def create_sqrt_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_sqrt_matrix(n)

for i in range(len(mat_1)):
    row = mat_1[i]
    score = sum(row)
    average = score / len(row)
    count = 0

    for j in range(len(row)):
        if row[j] > average:
            count += 1

    print(count)