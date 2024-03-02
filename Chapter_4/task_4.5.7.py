def create_matrix(size):
    matrix = [input().split() for _ in range(size)]
    for i in range(size):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix


n = int(input())
mat_1 = create_matrix(n)

for i in range(n):
    ls = list()

    for j in range(n):
        ls.append(mat_1[n-j-1][i])

    print(*ls)
