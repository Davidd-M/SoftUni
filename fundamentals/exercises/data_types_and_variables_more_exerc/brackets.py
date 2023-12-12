lines = int(input())
open_brackets = 0
closed_brackets = 0
last_char = ''
unbalanced = False
for _ in range(lines):
    char = input()
    if char == '(':
        if last_char == '(':
            unbalanced = True
        else:
            open_brackets += 1
            last_char = '('
    elif char == ')':
        if last_char == ')' or last_char != '(':
            unbalanced = True
        else:
            closed_brackets += 1
            last_char = ')'
if open_brackets != closed_brackets:
    unbalanced = True
if unbalanced:
    print('UNBALANCED')
else:
    print('BALANCED')
