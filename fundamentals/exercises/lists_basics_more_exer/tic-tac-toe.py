def row_win(board):
    for row in board:
        if all(element == row[0] for element in row):
            if row[0] == '1':
                print("First player won")
                exit()
            elif row[0] == '2':
                print("Second player won")
                exit()


def column_win(board):
    for i in range(2):
        if board[i][i] == board[1][i] and board[i][i] == board[2][i]:
            if board[i][i] == '1':
                print("First player won")
                exit()
            elif board[i][i] == '2':
                print("Second player won")
                exit()


def diagonal_win(board):
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == '1':
            print("First player won")
            exit()
        elif board[0][0] == '2':
            print("Second player won")
            exit()
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] == '1':
            print("First player won")
            exit()
        elif board[0][2] == '2':
            print("Second player won")
            exit()


row_1 = input().split()
row_2 = input().split()
row_3 = input().split()
board = [row_1, row_2, row_3]
row_win(board)
column_win(board)
diagonal_win(board)
print("Draw!")
