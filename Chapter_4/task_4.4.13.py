# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы диагоналей также учитываются.

from math import *


def create_sqrt_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_sqrt_matrix(n)
point = ceil(len(mat_1) / 2)
num = max(mat_1[0][0], mat_1[0][-1])

for i in range(1, point):
    for j in range(i+1):
        if max(mat_1[i][j], mat_1[i][n-j-1]) > num:
            num = max(mat_1[i][j], mat_1[i][n-j-1])

for i in range(point):
    for j in range(i+1):
        if max(mat_1[n-i-1][j], mat_1[n-i-1][n-j-1]) > num:
            num = max(mat_1[n-i-1][j], mat_1[n-i-1][n-j-1])

print(num)
