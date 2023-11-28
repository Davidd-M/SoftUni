'''
You will be given strings until you receive the command "End". For each string given, you should print a string in
which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni", you should
NOT print it!
'''
stri = ''
while True:
    stri = input()
    if stri == 'End':
        break
    if stri == 'SoftUni':
        continue
    new_str = ''
    for index, letter in enumerate(stri):
        new_str += letter + stri[index]
    print(new_str)

