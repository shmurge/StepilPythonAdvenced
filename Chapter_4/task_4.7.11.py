# Напишите программу, которая возводит квадратную матрицу в m-ую степень.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы,
# затем натуральное число m.
#
# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.


def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
matrix_1 = create_matrix(n)
m = int(input())
matrix_2 = matrix_1.copy()
matrix_3 = list()
count = 1

while count < m:
    matrix_4 = list()

    for i in range(len(matrix_1)):
        ls = list()
        row = matrix_1[i]

        for j in range(n):
            mult = 0

            for k in range(n):
                mult += row[k] * matrix_2[k][j]

            ls.append(mult)

        matrix_4.append(ls)

    matrix_1 = matrix_4.copy()
    count += 1

for row in range(n):
    print(*matrix_1[row])