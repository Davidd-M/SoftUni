text = input()
count_dict = {}

for char in text:
    if char == " ":
        continue
    elif char not in count_dict:
        count_dict[char] = 0
    count_dict[char] += 1

for k, v in count_dict.items():
    print(f"{k} -> {int(v)}")