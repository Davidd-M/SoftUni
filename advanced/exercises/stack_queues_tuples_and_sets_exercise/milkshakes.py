from collections import deque

chocolates = deque(map(int, input().split()))
cups = deque(map(int, input().split())).rotate(-1)

print(cups)
for char1, char2 in chocolates, cups:
    if char1 == char2:
        pass