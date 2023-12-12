input_str = input()
encrypted_str = ""
for character in input_str:
    encrypted_str += chr(ord(character) + 3)
print(encrypted_str)