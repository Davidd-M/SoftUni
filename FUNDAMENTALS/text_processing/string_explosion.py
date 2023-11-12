input_string = input()
new_string = ""
strength = 0

for index in range(len(input_string)):
    if strength > 0 and input_string[index] != ">":
        strength -= 1
    elif input_string[index] == ">":
        new_string += ">"
        strength += int(input_string[index + 1])
    else:
        new_string += input_string[index]
print(new_string)