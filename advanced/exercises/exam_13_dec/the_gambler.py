board = []
gambler_pos = ()
entering_amount = 100
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(int(input())):
    row = list(input())

    if "G" in row:
        col_index = row.index("G")
        gambler_pos = (row_index, col_index)
    board.append(row)


while True:
    command = input()

    if command == "end":
        print(f"End of the game. Total amount: {entering_amount}$")
        break

    next_row, next_col = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if next_row >= len(board) or next_col >= len(board):
        print(f"Game over! You lost everything!")
        break

    board[gambler_pos[0]][gambler_pos[1]] = "-"

    if board[next_row][next_col] == "W":
        entering_amount += 100

    elif board[next_row][next_col] == "P":
        entering_amount -= 200
        if entering_amount <= 0:
            print(f"Game over! You lost everything!")
            break

    elif board[next_row][next_col] == "J":
        entering_amount += 100000
        board[gambler_pos[0]][gambler_pos[1]] = "G"
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {entering_amount}$")
        break

    gambler_pos = (next_row, next_col)
    board[gambler_pos[0]][gambler_pos[1]] = "G"

if entering_amount > 0:
    [print(*row, sep="") for row in board]