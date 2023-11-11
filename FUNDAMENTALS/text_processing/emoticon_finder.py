input_list = input().split(":")
input_list.pop(0)
for sequence in input_list:
    emoji = sequence[:1]
    print(f":{emoji}")