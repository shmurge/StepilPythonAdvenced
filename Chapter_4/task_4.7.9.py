# Напишите программу для вычисления суммы двух матриц.
#
# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах,
# затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.


def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


nums = input().split()
n = int(nums[0])
m = int(nums[1])

matrix_1 = create_matrix(n)
input()
matrix_2 = create_matrix(n)
matrix_3 = list()

for i in range(n):
    ls = list()

    for j in range(m):
        ls.append(matrix_1[i][j]+matrix_2[i][j])

    matrix_3.append(ls)

for row in range(n):
    print(*matrix_3[row])
