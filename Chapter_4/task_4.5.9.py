# Магическим квадратом порядка n называется квадратная таблица размера n×n,
# составленная из всех чисел 1,2,3,…,n^2(то есть все числа разные) так, что суммы по каждому столбцу,
# каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, которая проверяет,
# является ли заданная квадратная матрица магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы:
# n строк, по n чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.


def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_matrix(n)
score = sum(mat_1[0])
flag = True


if flag:
    flag = False
    for i in range(1, n):
        if mat_1[0] != mat_1[i]:
            flag = True
            break

if flag:
    for i in range(1, n):
        if flag:
            for j in range(n):
                if mat_1[i][j] in mat_1[i-1]:
                    flag = False
                    break

if flag:
    for row in range(1, n):
        if sum(mat_1[row]) != score:
            flag = False
            break

if flag:
    for col in range(n):
        summ = 0
        for row in range(n):
            if mat_1[row][col] == 0:
                flag = False
                break
            summ += mat_1[row][col]
        if summ != score:
            flag = False
            break

if flag:
    main_sum = 0
    side_sum = 0
    for i in range(n):
        main_sum += mat_1[i][i]
        side_sum += mat_1[i][n-i-1]
    if main_sum != side_sum:
        flag = False

if flag:
    print("YES")
else:
    print("NO")
