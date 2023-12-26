rows, cols = input().split()

matrix = []

for row in range(int(rows)):
    current_row = []
    first_letter = chr(97 + row)
    last_letter = chr(97 + row)
    for col in range(int(cols)):
        middle_letter = chr(97 + col + row)
        current_row.append(first_letter + middle_letter + last_letter)
    matrix.append(current_row)

[print(*el) for el in matrix]
