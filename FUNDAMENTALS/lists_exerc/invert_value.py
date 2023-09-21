str_input = input()
my_list = str_input.split()
new_list = []
for num in my_list:
    num = int(num)
    if num > 0:
        num = num - 2 * num
    else:
        num += -2 * num
    new_list.append(num)

print(new_list)