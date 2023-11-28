number = int(input())
word = input()
empty_list = []
for strings in range(number):
    words = input()
    empty_list.append(words)
print(empty_list)
for i in range(len(empty_list) -1, -1, -1):
    if word not in empty_list[i]:
        empty_list.remove(empty_list[i])
print(empty_list)