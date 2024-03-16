# Латинским квадратом порядка n называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n. Напишите программу,
# которая проверяет, является ли заданная квадратная матрица латинским квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы:
# n строк, по n чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является латинским квадратом, и слово NO, если не является.

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
    if not flag:
        break
    rows = mat_1[i].copy()
    cols = list()

    for j in range(len(mat_1)):
        cols.append(mat_1[j][i])

    for k in range(1, n+1):
        if k not in rows or k not in cols:
            flag = False
            break

if flag:
    print("YES")
else:
    print("NO")