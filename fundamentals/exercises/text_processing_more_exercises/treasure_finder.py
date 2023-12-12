key_list = list(map(int, input().split()))
strings = []
results = []

while True:
    command = input()
    if command == "find":
        break
    strings.append(command)
for current_string in strings:
    current_treasure = ""
    for i, str_char in enumerate(current_string):
        key = key_list[i % len(key_list)]
        current_treasure += (chr(ord(str_char) - key))
    results.append(current_treasure)

for treasure in results:
    type_start = treasure.find("&")
    type_end = treasure.find("&", treasure.find("&") + 1)
    coordinate_start = treasure.find("<") + 1
    coordinate_end = treasure.find(">")
    print(f"Found {treasure[type_start+1:type_end]} at {treasure[coordinate_start:coordinate_end]}")