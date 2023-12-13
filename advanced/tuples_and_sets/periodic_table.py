n = int(input())

unique_elements = set()

for _ in range(n):
    line = input()
    for el in (line.split()):
        unique_elements.add(el)

print(*unique_elements, sep='\n')
