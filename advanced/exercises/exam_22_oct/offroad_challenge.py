from collections import deque

initial_fuel = list(map(int, input().split()))
consumption = deque(map(int, input().split()))
fuel_needed = deque(map(int, input().split()))
reached_altitudes = []

for altitude in range(1, 5):
    last_fuel_quantity = initial_fuel.pop()
    first_consumption_index = consumption.popleft()
    subtract_result = last_fuel_quantity - first_consumption_index
    if subtract_result >= fuel_needed[0]:
        print(f"John has reached: Altitude {altitude}")
        reached_altitudes.append(f"Altitude {altitude}")
        fuel_needed.popleft()
    else:
        print(f"John did not reach: Altitude {altitude}")
        break

if 0 < len(fuel_needed) < 4:
    print("John failed to reach the top.\nReached altitudes: ", end='')
    print(*reached_altitudes, sep=', ')
elif not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif len(reached_altitudes) == 4:
    print("John has reached all the altitudes and managed to reach the top!")

