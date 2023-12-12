input_strings = input().split()
total_sum = 0

for string in input_strings:
    first_letter = string[0]
    last_letter = string[len(string) - 1]
    first_position = ord(first_letter.lower()) - 96
    last_position = ord(last_letter.lower()) - 96
    number = ''
    for index in range(1, len(string) - 1):
        number += string[index]
    number = int(number)
    if first_letter.isupper():
        number = number / first_position
    elif first_letter.islower():
        number = number * first_position
    if last_letter.isupper():
        number = number - last_position
    elif last_letter.islower():
        number = number + last_position
    total_sum += number

print(f"{total_sum:.2f}")
