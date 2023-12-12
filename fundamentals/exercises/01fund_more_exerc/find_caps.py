word = input()
empty_list = []
for i, letter in enumerate(word):
    if letter.isupper():
        empty_list.append(i)
print(empty_list)