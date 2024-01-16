from functools import reduce


input_list = input().split()
nums_list = []
is_negative_integer = lambda s: s.startswith('-') and s[1:].isdigit()
functions = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y,
    "*": lambda x, y: x * y
}

for char in input_list:
    if char.isnumeric():
        nums_list.append(int(char))
    elif is_negative_integer(char):
        nums_list.append(int(char))
    else:
        nums_list = [reduce(functions[char], nums_list)]

print(*nums_list)

# 6 3 - 2 1 * 5 /