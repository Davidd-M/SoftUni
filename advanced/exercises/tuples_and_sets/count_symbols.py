my_var = tuple(input())

for char in sorted(set(my_var)):
    print(f"{char}: {my_var.count(char)} time/s")
    