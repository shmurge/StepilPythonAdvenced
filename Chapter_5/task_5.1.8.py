# На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n
# и заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, – число 1;
# на следующих двух диагоналях – число 2, и т.д.

def create_matrix_sample(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = abs(i - j)

    return matrix

# Создаем и выводим образцовую матрицу
n = int(input())
matrix = create_matrix_sample(n)
for row in matrix:
    print(' '.join(map(str, row)))