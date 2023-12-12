input_string = input()

for index, character in enumerate(input_string):
    if character == ":":
        print(f":{input_string[index + 1]}")
