char1 = input()
char2 = input()

def chars_in_between(char1, char2):
    chars_list = []
    char1= ord(char1)
    char2 = ord(char2)
    for i in range(char1 + 1, char2):
        chars_list.append(chr(i))
    return chars_list
chars_list = chars_in_between(char1, char2)
result = ' '.join(chars_list)
print(result)