input_string = input()
numbers_list = []
chars_list = []

for i, char in enumerate(input_string):
    if char.isdigit():
        numbers_list.append(char)   # digit or str ?!
    else:
        chars_list.append(char)

take_list = []
skip_list = []

for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

string_to_print = ''

for i in range(len(take_list)):
    chars_to_take = int(take_list[i])
    chars_to_skip = int(skip_list[i])
    taken_string = chars_list[:chars_to_take]
    chars_list[:chars_to_take] = []
    skipped_string = chars_list[:chars_to_skip]
    chars_list[:chars_to_skip] = []
    string_to_print += ''.join(taken_string)
print(string_to_print)

