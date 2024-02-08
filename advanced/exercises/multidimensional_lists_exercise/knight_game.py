board = [list(input()) for _ in range(int(input()))]
moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)
removed_knights = 0


while True:
    max_attacks = 0
    knight_coordinates = ()
    for row in range(len(board)):
        current_row = board[row]
        for col in range(len(current_row)):
            if board[row][col] == "K":
                attacks = 0
                for pos in moves:
                    row_move = pos[0] + row
                    col_move = pos[1] + col
                    if 0 <= row_move < len(board) and 0 <= col_move < len(current_row):
                        if board[row_move][col_move] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_coordinates = (row, col)
    if knight_coordinates:
        board[knight_coordinates[0]][knight_coordinates[1]] = 0
        removed_knights += 1
    else:
        break
print(removed_knights)