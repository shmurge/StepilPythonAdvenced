# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов
# в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке;
# подряд идут элементы сначала первой строки, затем второй, и т.д.

# Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

# Формат входных данных
# На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов,
# каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.

n = int(input())
m = int(input())


def create_matrix(rows, cols):
    matrix = list()
    ls = list()
    for _ in range(rows):
        ls = []
        for _ in range(cols):
            word = input()
            ls.append(word)
        matrix.append(ls)

    return matrix


def print_matrix(matrix, width=1):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()


mat_1 = create_matrix(n, m)
print_matrix(mat_1)
