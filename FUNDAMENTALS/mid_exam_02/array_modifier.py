def swap_func(int_list, index1, index2):
    int_list[index1], int_list[index2] = int_list[index2], int_list[index1]
    return int_list


def multiply_func(int_list, index1, index2):
    result = int_list[index1] * int_list[index2]
    int_list[index1] = result
    return int_list


integers_list = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'end':
        break
    elif command[0] == "swap":
        integers_list = swap_func(integers_list, int(command[1]), int(command[2]))
    elif command[0] == "multiply":
        integers_list = multiply_func(integers_list, int(command[1]), int(command[2]))
    elif command[0] == "decrease":
        integers_list = [x - 1 for x in integers_list]
integers_list = [str(x) for x in integers_list]
print(', '.join(integers_list))
