initial_energy = int(input())
won_battles = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
        break
    distance = int(distance)
    if initial_energy - distance < 0:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break
    won_battles += 1
    initial_energy -= distance
    if won_battles % 3 == 0:
        initial_energy += won_battles
    