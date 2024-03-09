from collections import deque

armor_sequence = deque(int(x) for x in input().split(","))
strikes = list(map(int, input().split(",")))
killed = 0

while armor_sequence and strikes:
    monster = armor_sequence.popleft()
    strike = strikes.pop()

    if strike >= monster:
        killed += 1
        strike -= monster
        if strike > 0:
            if strikes:
                strikes[len(strikes) - 1] += strike
            else:
                strikes.append(strike)

    else:
        armor_sequence.append(monster - strike)

if not armor_sequence:
    print("All monsters have been killed!")

if not strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed}")

