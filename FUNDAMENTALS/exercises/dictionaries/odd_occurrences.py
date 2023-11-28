input_list = input().split()

occurrences_dict = {}

for word in input_list:
    word = word.lower()
    if word not in occurrences_dict:
        occurrences_dict[word] = 0
    occurrences_dict[word] += 1

for word, occurrence in occurrences_dict.items():
    if occurrence % 2 != 0:
        print(f"{word}", end=" ")