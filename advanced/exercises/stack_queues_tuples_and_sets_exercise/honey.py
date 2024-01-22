from collections import deque


def honey_calc(a_bee, a_symbol, a_nectar):
    try:
        return abs(symbols_map[a_symbol](a_bee, a_nectar))
    except ZeroDivisionError:
        return 0


bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())
total_honey = 0
symbols_map = {
    "-": lambda x, y: x-y,
    "+": lambda x, y: x+y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y,
}

while bees and nectar:
    current_nectar = nectar.pop()
    current_bee = bees.popleft()
    if current_nectar >= current_bee:
        total_honey += honey_calc(current_bee, symbols.popleft(), current_nectar)
    else:
        bees.appendleft(current_bee)
        continue

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")

