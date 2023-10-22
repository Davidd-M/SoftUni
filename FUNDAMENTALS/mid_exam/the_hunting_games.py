adventure_days = int(input())
players_number = int(input())
energy = float(input())
daily_water_per_person = float(input())
daily_food_per_person = float(input())
water = players_number * daily_water_per_person * adventure_days
food = players_number * daily_food_per_person * adventure_days


for day in range(1, adventure_days + 1):
    energy_lost = float(input())
    energy -= energy_lost
    if energy <= 0:
        print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
        exit()
    if day % 2 == 0:
        energy *= 1.05
        water *= 0.7
    if day % 3 == 0:
        food -= food / players_number
        energy *= 1.1
print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
