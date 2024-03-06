from collections import deque

worms = input().split()
holes = deque(input().split())
matches = 0
total_worms = len(worms)

while worms and holes:
    last_worm = int(worms.pop())
    first_hole = int(holes.popleft())

    if last_worm != first_hole:
        if last_worm - 3 > 0:
            worms.append(last_worm - 3)  # TODO WHAT IF ALREADY < 0
        continue

    matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and total_worms == matches:
    print("Every worm found a suitable hole!")
elif worms:
    print(f"Worms left: {', '.join(map(str, worms))}")
else:
    print("Worms left: none")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(map(str, holes))}")
