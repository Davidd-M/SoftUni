integers = input().split()
count = int(input())
smallest_num = 0
for n in range(count):
    smallest_num = int(integers[0])
    for i, num in enumerate(integers):
        if int(num) < int(smallest_num):
            smallest_num = num
    integers.remove(str(smallest_num))
print(', '.join(integers))
