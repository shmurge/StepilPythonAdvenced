# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.


def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_matrix(n)
num = mat_1[0][-1]

for i in range(1, n):
    for j in range(i+1):
        if mat_1[i][n-j-1] > num:
            num = mat_1[i][n-j-1]

print(num)
