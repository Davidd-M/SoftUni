from collections import deque

clothes = deque(map(int, input().split()))
rack_capacity = int(input())
racks_used = 1
current_capacity = 0

while clothes:
    if current_capacity + clothes[0] <= rack_capacity:
        current_capacity += clothes.popleft()
    else:
        racks_used += 1
        current_capacity = 0
print(racks_used)
