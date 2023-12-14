matrix = [input().split(", ") for _ in range(int(input()))]
primary = []
secondary = []

for i in range(len(matrix)):
    primary.append(matrix[i][i])
    secondary.append(matrix[i][-(i+1)])

print(f"Primary diagonal: {', ' .join(primary)}. Sum: {sum([int(el) for el in primary])}")
print(f"Secondary diagonal: {', '.join(secondary)}. Sum: {sum([int(el) for el in secondary])}")
