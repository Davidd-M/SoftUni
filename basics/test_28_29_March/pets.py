days = int(input())
total_food = float(input())
biscuit_total = 0
both_eaten_total = 0
cats_eaten = 0
dogs_eaten = 0

for day in range(1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())
    dogs_eaten += dog_eaten
    cats_eaten += cat_eaten
    both_eaten = cat_eaten + dog_eaten
    both_eaten_total += both_eaten
    if day % 3 == 0 and day != 0:
        biscuit = 0.1 * both_eaten
        biscuit_total += biscuit
percent = both_eaten_total / total_food * 100
dog_percent = dogs_eaten / both_eaten_total * 100
cat_percent = cats_eaten / both_eaten_total * 100

print(f"Total eaten biscuits: {round(biscuit_total)}gr.")
print(f"{percent:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")
