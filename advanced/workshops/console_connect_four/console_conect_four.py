class FullColumnError(Exception):
    pass


class InvalidColumn(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTIONS_MAP = {
    "left": (0, -1),
    "down": (1, 0),
    "bottom_right": (1, 1),
    "bottom_left": (1, -1),
}


def is_winner(current_row, current_col, board):
    searched_element = board[current_row][current_col]

    for direction, (r, c) in DIRECTIONS_MAP.items():
        count = 1

        for i in range(1,4):
            new_row = current_row + r * i
            new_col = current_col + c * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                break

            if board[new_row][new_col] != searched_element:
                break

            count += 1

        for i in range(1,4):
            new_row = current_row - r * i
            new_col = current_col - c * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
                break

            if board[new_row][new_col] != searched_element:
                break

            count += 1

        if count >= 4:
            return True
    return False


def print_board(board):
    for row in board:
        print(row)


def validate_column(col):
    if 0 <= col < COLS:
        return True
    raise InvalidColumn


def place_player_choice(col_index, board):
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError("The selected column full!")


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        if turns == 43:
            print('Draw')
            quit()
        column = int(input(f"Player {player}, please choose a column: "))
        column_index = column - 1
        validate_column(column_index)
        row = place_player_choice(column_index, board)
        board[row][column_index] = player

        if is_winner(row, column_index, board):
            print_board(board)
            print(f'Player {player} won!')
            exit()

    except FullColumnError as e:
        print(f"{e}")
        continue

    except InvalidColumn:
        print("The selected column is invalid!")
        continue

    except ValueError:
        print("Please enter a valid number!")

    print_board(board)
    turns += 1
