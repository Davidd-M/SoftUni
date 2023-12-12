'''
You will be given two strings. Transform the first string into the second one, letter by letter, starting from the first
one. After each interaction, print the resulting string only if it is unique.
Note: the strings will have the same length.
Ditty
Dotty
Dogty
Doggy
'''
str1 = input()
str2 = input()
current_str = str1
for i in range(len(str1)):
    if current_str[i] != str2[i]:
        current_str = current_str[:i] + str2[i] + current_str[i+1:]
        if current_str != str2:
            print(current_str)
print(current_str)


