matrix = [input().split() for _ in range(int(input()))]
primary = []
secondary = []

for i in range(len(matrix)):
    primary.append(int(matrix[i][i]))
    secondary.append(int(matrix[i][-(i+1)]))

primary_sum, secondary_sum = sum(primary), sum(secondary)

print(f"{abs(primary_sum - secondary_sum)}")
