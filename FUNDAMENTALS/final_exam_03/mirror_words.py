import re

my_string = input()

pattern = r"(@|#)([a-zA-Z]{3,})(\1){2}([a-zA-Z]{3,})\1"
matches = re.findall(pattern, my_string)
mirror_words = []
for index in range(0, len(matches)):
    if matches[index][1] == matches[index][3][::-1]:
        mirror_words.append(matches[index][1] + ' <=> ' + matches[index][3])
if not matches:
    print("No word pairs found!")
if matches:
    print(f"{len(matches)} word pairs found!")
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))
