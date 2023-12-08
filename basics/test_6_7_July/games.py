games_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(games_sold):
    name = input()
    if name == 'Hearthstone':
        hearthstone += 1
    elif name == 'Fornite':
        fornite += 1
    elif name == 'Overwatch':
        overwatch += 1
    else:
        others += 1

percent_hearthstone = (hearthstone / games_sold) * 100
percent_fornite = (fornite / games_sold) * 100
percent_overwatch = (overwatch / games_sold) * 100
percent_others = (others / games_sold) * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
