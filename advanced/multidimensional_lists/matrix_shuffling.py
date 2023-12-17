def valid_coordinates(matrix_rows, matrix_cols, ranges):
    if len(ranges) != 5:
        return False
    check_row1, check_col1, check_row2, check_col2 = [int(x) for x in ranges[1:5]]
    if check_row1 not in range(rows) and check_col1 not in range(cols):
        return False
    if check_row2 not in range(rows) and check_col2 not in range(cols):
        return False
    return True


rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    elif command[0] == "swap":
        if valid_coordinates(rows, cols, command):
            row1, col1, row2, col2 = [int(x) for x in command[1:5]]
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*el) for el in matrix]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

