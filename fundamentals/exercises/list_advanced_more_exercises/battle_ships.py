field = [[int(x) for x in input().split()] for r in range(int(input()))]

attacked_squares = input().split()
destroyed = 0

for attacked_square in attacked_squares:
    attacked_row, attacked_col = map(int, attacked_square.split("-"))
    if field[attacked_row][attacked_col] > 0:
        field[attacked_row][attacked_col] -= 1
        if field[attacked_row][attacked_col] == 0:
            destroyed += 1

print(destroyed)
