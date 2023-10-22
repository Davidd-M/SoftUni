numbers_list = input().split(", ")
group = 0

while True:
    group += 10
    numbers_group = [int(x) for x in numbers_list if int(x) <= group]
    numbers_list = [int(x) for x in numbers_list if int(x) > group]
    print(f"Group of {group}'s: {numbers_group}")
    if not numbers_list:
        break
