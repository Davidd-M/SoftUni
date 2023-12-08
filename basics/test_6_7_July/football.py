club_name = input()
matches = int(input())

if matches == 0:
    print(f"{club_name} hasn't played any games during this season.")
    quit()
points = 0
games_won = 0
games_drawn = 0
games_lost = 0
for i in range(matches):
    result = input()
    if result == 'W':
        points += 3
        games_won += 1
    if result == 'D':
        points += 1
        games_drawn += 1
    if result == 'L':
        points += 0
        games_lost +=1

percent_won = (games_won / matches) * 100

print(f"{club_name} has won {points} points during this season.")
print(f"Total stats:")
print(f"## W: {games_won}")
print(f"## D: {games_drawn}" )
print(f"## L: {games_lost}" )
print(f"Win rate: {percent_won:.2f}%")