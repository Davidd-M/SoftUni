food_bought = int(input()) * 1000
eaten_total = 0
while True:
    eaten = input()
    if eaten == 'Adopted':
        break
    eaten_total += int(eaten)
diff = abs(food_bought - eaten_total)
if eaten_total > food_bought:
    print(f"Food is not enough. You need {diff} grams more.")
elif eaten_total <= food_bought:
    print(f"Food is enough! Leftovers: {diff} grams.")