people_list = input().split()
skips = int(input())
index = 0
output = []

while people_list:
    index = (index + skips - 1) % len(people_list)
    output.append(people_list.pop(index))

print(output)
