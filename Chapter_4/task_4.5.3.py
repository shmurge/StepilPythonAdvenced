# Напишите программу, которая меняет местами столбцы в матрице.

# Формат входных данных
# На вход программе на разных строках подаются два натуральных числа
# n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел,
# затем числа i и j — номера столбцов, подлежащих обмену.

# Формат выходных данных
# Программа должна вывести указанную таблицу с замененными столбцами.


n = int(input())
m = int(input())
matrix = [input().split() for _ in range(n)]

for r in range(n):
    for c in range(len(matrix[r])):
        matrix[r][c] = int(matrix[r][c])

i_j_ls = input().split()
i = int(i_j_ls[0])
j = int(i_j_ls[1])

for r in range(len(matrix)):
    matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
    print(*matrix[r])

