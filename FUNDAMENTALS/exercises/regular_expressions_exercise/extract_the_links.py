import re

pattern = r"www.[a-zA-Z0-9-]+\.\b[a-z-.]+"
text = input()
while text:
    link = re.findall(pattern, text)
    if link:
        print(*link)
    text = input()
