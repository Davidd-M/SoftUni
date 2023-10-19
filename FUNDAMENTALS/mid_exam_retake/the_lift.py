people_waiting = int(input())
lift_state = list(map(int, input().split()))

for index, lift in enumerate(lift_state):
    diff = 4 - lift
    if diff > people_waiting:
        lift_state[index] += people_waiting
        if lift_state[index] > 4:
            people_waiting = lift_state[index] - 4
            lift_state[index] = 4
            continue
        people_waiting = 0
        print("The lift has empty spots!")
        print(*lift_state)
        exit()
    else:
        people_waiting -= diff
        lift_state[index] += diff
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift_state)
elif people_waiting == 0:
    print(*lift_state)
