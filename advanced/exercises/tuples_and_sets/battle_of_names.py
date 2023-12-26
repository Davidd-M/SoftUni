n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n+1):
    name = input()
    ascii_value = 0
    for char in name:
        ascii_value += ord(char)
    ascii_value = int(ascii_value // row)
    even_set.add(ascii_value) if ascii_value % 2 == 0 else odd_set.add(ascii_value)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) >= sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) <= sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")
