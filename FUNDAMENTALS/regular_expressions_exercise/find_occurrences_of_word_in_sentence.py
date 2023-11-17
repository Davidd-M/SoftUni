import re

sentence = input()
searched_word = input()
result = re.findall(rf"(?i)\b{searched_word}+\b", sentence)
print(len(result))
