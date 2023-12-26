from collections import deque

opening_parentheses = deque()

for char in input():
    if char == "(" or char == "[" or char == "{":
        opening_parentheses.append(char)
    elif not opening_parentheses:
        print("NO")
        break
    else:
        if opening_parentheses.pop() + char not in "()[]{}":
            print("NO")
            break
else:
    print("YES")
