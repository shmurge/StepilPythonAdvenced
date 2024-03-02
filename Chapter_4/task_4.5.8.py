# На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
# которые бьёт конь. Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьёт конь,
# отметьте символами *, остальные клетки заполните точками.

# Формат входных данных
# На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в виде e4,
# где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру строки
# (цифра от 1 до 8, снизу вверх).

# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

n = 8
chess_board = [["."]*n for _ in range(n)]
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
knight = input()
col = cols.index(knight[0])
row = int(knight[1])
chess_board[n-row][col] = 'N'

if col+1 <= len(chess_board) - 1 and row + 2 <= len(chess_board):
    chess_board[n-row-2][col+1] = "*"
if col+1 <= len(chess_board) - 1 and row - 2 > 0:
    chess_board[n-row+2][col+1] = "*"
if col+2 <= len(chess_board) - 1 and row + 1 <= len(chess_board):
    chess_board[n-row-1][col+2] = "*"
if col+2 <= len(chess_board) - 1 and row - 1 > 0:
    chess_board[n-row+1][col+2] = "*"
if col-1 >= 0 and row + 2 <= len(chess_board):
    chess_board[n-row-2][col-1] = "*"
if col-1 >= 0 and row - 2 > 0:
    chess_board[n-row+2][col-1] = "*"
if col-2 >= 0 and row + 1 <= len(chess_board):
    chess_board[n-row-1][col-2] = "*"
if col-2 >= 0 and row - 1 > 0:
    chess_board[n-row+1][col-2] = "*"

for r in range(n):
    for c in range(n):
        print(chess_board[r][c], end=' ')
    print()