input_string = input().upper()
non_digits = []
string_to_multiply = ""
multiply_by = ''

for index in range(len(input_string)):
    if input_string[index].isdigit():
        for character in input_string[index:]:
            if character.isdigit():
                multiply_by += character
            else:
                break
        non_digits.append(string_to_multiply * int(multiply_by))
        multiply_by = ''
        string_to_multiply = ''
    else:
        string_to_multiply += input_string[index]
length = ''.join(non_digits)
print(f"Unique symbols used: {len(set(str(length)))}")
print(''.join(non_digits))


