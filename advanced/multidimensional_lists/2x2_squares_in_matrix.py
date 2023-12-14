rows, cols = input().split()

matrix = [input().split() for row in range(int(rows))]
matches = 0

for row in range(int(rows) - 1):
    for col in range(int(cols) - 1):
        if matrix[row][col] == matrix[row][col + 1] and \
                matrix[row][col] == matrix[row + 1][col] and \
                matrix[row][col] == matrix[row + 1][col + 1]:
            matches += 1

print(matches)