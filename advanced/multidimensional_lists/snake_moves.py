rows, cols = [int(el) for el in input().split()]

snake_string = input()
matrix = []
start_index = -1

for row in range(rows):
    curr_row = []
    end_str = cols % len(snake_string)
    for col in range(cols):
        start_index += 1
        curr_row.append(snake_string[start_index % len(snake_string)])
    if len(matrix) % 2 == 0:
        matrix.append(curr_row)
    else:
        matrix.append(curr_row[::-1])

[print(*el, sep="") for el in matrix]