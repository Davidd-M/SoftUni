lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_brakes = 0
for loss in range(1, lost_fights + 1):
    broken_helmet = False
    broken_sword = False
    if loss % 2 == 0:
        expenses += helmet_price
        broken_helmet = True
    if loss % 3 == 0:
        expenses += sword_price
        broken_sword = True
    if broken_sword and broken_helmet:
        expenses += shield_price
        shield_brakes += 1
        if shield_brakes % 2 == 0:
            expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")