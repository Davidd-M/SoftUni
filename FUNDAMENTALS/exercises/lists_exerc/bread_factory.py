energy = 100
coins = 100
events = input().split("|")
completed = True
for event in events:
    event_or_ingredient, num = event.split("-")
    num = int(num)
    if event_or_ingredient == "rest":
        if energy + num > 100:
            num = 100 - energy
            energy = 100
        else:
            energy += num
        print(f"You gained {num} energy.")
        print(f"Current energy: {energy}.")
    elif event_or_ingredient == "order":
        energy -= 30
        if energy >= 0:
            coins += num
            print(f"You earned {num} coins.")
        else:
            energy += 80
            print("You had to rest!")
    else:
        coins -= num
        if coins >= 0:
            print(f"You bought {event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            completed = False
            break
if completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
