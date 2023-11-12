input_string = input()
last_character = ""
string_to_print = ""

for index, character in enumerate(input_string):
    if character != last_character:
        string_to_print += character
    last_character = character

print(string_to_print)