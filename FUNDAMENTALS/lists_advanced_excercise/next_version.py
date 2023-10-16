input_version = input().split(".")
x1, x2, x3 = int(input_version[0]), int(input_version[1]), int(input_version[2])

x3 += 1
if x3 > 9:
    x3 = 0
    x2 += 1
if x2 > 9:
    x2 = 0
    x1 += 1

next_version = f"{x1}.{x2}.{x3}"
print(next_version)
