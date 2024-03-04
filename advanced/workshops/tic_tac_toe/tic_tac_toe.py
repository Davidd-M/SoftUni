from collections import deque


def check_for_win():
    player_name, player_symbol = players[0].values()

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])
    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(SIZE)]) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")
        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0]["symbol"]

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print('DRAW!')
        raise SystemExit

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']} choose a position: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print("Invalid position!")
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":
            turns += 1
            place_symbol(row, col)

        else:
            print_select_valid_pos_message()


def print_select_valid_pos_message():
    print("Please select a valid position")


def print_board(started=False):
    if started:
        print("\n".join(["| " + " | ".join(row) + " |" for row in board]))
        for row_index in range(SIZE):
            for col_index in range(SIZE):
                board[row_index][col_index] = " "
    else:
        print("\n".join(["| " + " | ".join(row) + " |" for row in board]))


def start():
    player_one_name = input("Player1, please enter your name: ")
    player_two_name = input("Player2, please enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one_name}, would like to play with X or O: ").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name}, please select a valid option")
            continue

        player_two_symbol = "O" if player_one_symbol == "X" else "X"
        break

    players.append({"name": player_one_name, "symbol": player_one_symbol})
    players.append({"name": player_two_name, "symbol": player_two_symbol})

    print_board(True)
    choose_position()


SIZE = 3
turns = 0

board = [[str(r + c) for c in range(3)] for r in range(1, 10, 3)]
players = deque()

start()
