n = int(input())
empty_list = []
required_list = []
for _ in range(n):
    ints = int(input())
    empty_list.append(ints)
command = input()
if command == 'even':
    for i in range(len(empty_list)):
        if empty_list[i] % 2 == 0:
            required_list.append(empty_list[i])
elif command == 'odd':
    for i in range(len(empty_list)):
        if empty_list[i] % 2 != 0:
            required_list.append(empty_list[i])
elif command == 'positive':
    for i in range(len(empty_list)):
        if empty_list[i] >= 0:
            required_list.append(empty_list[i])
elif command == 'negative':
    for i in range(len(empty_list)):
        if empty_list[i] < 0:
            required_list.append(empty_list[i])
print(required_list)