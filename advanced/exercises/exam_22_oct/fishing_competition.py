directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
my_pos = ()
matrix = []
fish = 0

for i in range(int(input())):
    row = list(input())
    matrix.append(row)
    if "S" in row:
        my_pos = (i, row.index("S"))

while True:
    command = input()
    if command == "collect the nets":
        break
    matrix[my_pos[0]][my_pos[1]] = "-"
    r, c = directions[command][0] + my_pos[0], directions[command][1] + my_pos[1]
    if r >= len(matrix):
        r = 0
    elif r < 0:
        r = len(matrix) - 1
    elif c >= len(matrix[r]):
        c = 0
    elif c < 0:
        c = len(matrix[r]) - 1
    if matrix[r][c] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{r},{c}]")
        exit()
    elif matrix[r][c].isdigit():
        fish += int(matrix[r][c])
    matrix[r][c] = "S"
    my_pos = (r, c)


if fish >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish} tons of fish more.")
if fish > 0:
    print(f"Amount of fish caught: {fish} tons.")

[print(*row, sep="") for row in matrix]