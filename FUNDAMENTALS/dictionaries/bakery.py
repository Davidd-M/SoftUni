input_list = input().split()

my_dict = {}

for i in range(0, len(input_list), 2):
    my_dict[input_list[i]] = int(input_list[i + 1])

print(my_dict)