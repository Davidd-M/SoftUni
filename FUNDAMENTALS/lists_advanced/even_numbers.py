input_list = input().split(", ")
print([index for index, number in enumerate(input_list) if int(number) % 2 == 0])
