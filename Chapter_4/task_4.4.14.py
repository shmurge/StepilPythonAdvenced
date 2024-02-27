# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
# верхнюю, нижнюю, левую и правую.

# Напишите программу, которая вычисляет сумму элементов:
# верхней четверти; правой четверти; нижней четверти; левой четверти.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы (целые числа) построчно через пробел.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Элементы диагоналей не учитываются.


def create_sqrt_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_sqrt_matrix(n)
up_score, right_score, down_score, left_score = 0, 0, 0, 0

for i in range(len(mat_1)):
    for j in range(len(mat_1[i])):
        if i < j and i < n-1-j:
            up_score += mat_1[i][j]
        elif j > i > n-1-j:
            right_score += mat_1[i][j]
        elif i > j and i > n-1-j:
            down_score += mat_1[i][j]
        elif j < i < n-1-j:
            left_score += mat_1[i][j]

print("Верхняя четверть:", up_score)
print("Правая четверть:", right_score)
print("Нижняя четверть:", down_score)
print("Левая четверть:", left_score)
