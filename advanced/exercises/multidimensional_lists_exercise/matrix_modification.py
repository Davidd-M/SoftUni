def valid_coordinate(row_idx, col_idx, matrix):
    if 0 <= row_idx < len(matrix) and 0 <= col_idx < len(matrix[row_idx]):
        return True
    return False


n = int(input())
matrix = [[int(d) for d in input().split()] for row in range(n)]

while True:
    command = input().split()
    if command[0] == "END":
        [print(*row) for row in matrix]
        break
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if not valid_coordinate(row, col, matrix):
        print("Invalid coordinates")
    elif command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value


