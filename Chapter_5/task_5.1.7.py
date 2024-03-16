# На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
# остальные клетки заполните точками.

def mark_attacked_cells(chess_notation):
    col_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    col = col_mapping[chess_notation[0]]
    row = int(chess_notation[1])

    board = [['.' for _ in range(8)] for _ in range(8)]

    for i in range(8):
        board[i][col - 1] = '*'  # Отмечаем все клетки на вертикали
        board[row - 1][i] = '*'  # Отмечаем все клетки на горизонтали

        if row - 1 - i >= 0 and col - 1 - i >= 0:
            board[row - 1 - i][col - 1 - i] = '*'  # Отмечаем клетки по диагонали вверх

        if row - 1 + i < 8 and col - 1 + i < 8:
            board[row - 1 + i][col - 1 + i] = '*'  # Отмечаем клетки по диагонали вниз

        if row - 1 - i >= 0 and col - 1 + i < 8:
            board[row - 1 - i][col - 1 + i] = '*'  # Отмечаем клетки по диагонали влево вниз

        if row - 1 + i < 8 and col - 1 - i >= 0:
            board[row - 1 + i][col - 1 - i] = '*'  # Отмечаем клетки по диагонали вправо вверх

    board[row - 1][col - 1] = 'Q'  # Поставим ферзя на указанную клетку

    for i in range(len(board)-1, -1, -1):
        print(*board[i])


# На вход подаем координаты ферзя
chess_position = input()
mark_attacked_cells(chess_position)