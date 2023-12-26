from collections import deque


def travel(stations):
    current_fuel = 0
    for station in stations:
        current_fuel += station["fuel"]
        current_fuel -= station["distance"]
        if current_fuel < 0:
            return False
    return True


n = int(input())
stations = deque()
index = 0

for _ in range(n):
    fuel, distance = input().split()
    stations.append({"fuel": int(fuel), "distance": int(distance)})

while not travel(stations):
    index += 1
    stations.rotate(-1)
    travel(stations)

print(index)
