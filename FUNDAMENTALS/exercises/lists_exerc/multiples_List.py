factor = int(input())
count = int(input())
empty_list = []
_ = 0
while len(empty_list) < count:
    _ += 1
    if _ % factor == 0:
        empty_list.append(_)
print(empty_list)
