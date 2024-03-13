# Напишите программу, которая перемножает две матрицы.
#
# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в первой матрице,
# затем элементы первой матрицы, затем пустая строка.
# Далее следуют числа m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


nums_1 = input().split()
n1 = int(nums_1[0])
m1 = int(nums_1[1])

matrix_1 = create_matrix(n1)
input()

nums_2 = input().split()
n2 = int(nums_2[0])
m2 = int(nums_2[1])
matrix_2 = create_matrix(n2)
matrix_3 = list()

for i in range(len(matrix_1)):
    ls = list()
    row = matrix_1[i]

    for j in range(m2):
        mult = 0

        for k in range(n2):
            mult += row[k] * matrix_2[k][j]

        ls.append(mult)

    matrix_3.append(ls)

for row in range(n1):
    print(*matrix_3[row])
