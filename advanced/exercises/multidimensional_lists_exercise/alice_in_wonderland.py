size = int(input())
matrix = []
alice_pos = ()
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
teas = 0

for i in range(size):
    current_row = input().split()
    matrix.append(current_row)
    if "A" in current_row:
        alice_pos = (i, current_row.index('A'))

while True:
    direction = input()
    row, col = alice_pos[0] + directions[direction][0], alice_pos[1] + directions[direction][1]
    matrix[alice_pos[0]][alice_pos[1]] = "*"
    if not (0 <= col < size and 0 <= row < size):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        print("Alice didn't make it to the tea party.")
        break
    elif matrix[row][col].isdigit():
        teas += int(matrix[row][col])
        if teas >= 10:
            matrix[row][col] = "*"
            print("She did it! She went to the party.")
            break
    alice_pos = (row, col)

[print(*row) for row in matrix]
