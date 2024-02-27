# Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.


def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_matrix(n)
flag = True

for i in range(len(mat_1)):
    rows = mat_1[i]
    cols = list()

    for j in range(len(mat_1)):
        cols.append(mat_1[j][i])

    if rows != cols:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")