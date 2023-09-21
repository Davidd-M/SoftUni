tournaments = int(input())
points_start = int(input())
variant = ""
variant_n = 0
variant_w = 0
points_tournaments = 0
for i in range(tournaments):
    variant = input()
    variant_n += 1
    if variant == "W":
        points_tournaments += 2000
        variant_w += 1
    elif variant == "F":
        points_tournaments += 1200
    elif variant == "SF":
        points_tournaments += 720

points_total = points_start + points_tournaments
average = points_tournaments / variant_n
won = (variant_w / tournaments) * 100

print(f"Final points: {int(points_total)}")
print(f"Average points: {int(average)}")
print(f"{won:.2f}%")
