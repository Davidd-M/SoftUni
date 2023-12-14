rows, cols = input().split()

matrix = [[int(el) for el in input().split()] for row in range(int(rows))]
max_sum = float("-inf")
submatrix = []

for row in range(int(rows) - 2):
    for col in range(int(cols) - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_sum:
            max_sum = current_sum
            submatrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for row in submatrix:
    print(*row)
