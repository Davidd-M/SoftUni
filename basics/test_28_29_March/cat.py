minutes_walk = int(input())
num_walks = int(input())
consumed_calories = int(input())

total_walked = minutes_walk * num_walks
burned_calorie = total_walked * 5

if burned_calorie >= consumed_calories/2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calorie}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calorie}.")
    