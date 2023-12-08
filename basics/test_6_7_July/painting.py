import math

height_wall = int(input())
width_wall = int(input())
percent_unpaintable = int(input())

walls_m2 = (height_wall * width_wall) * 4
unpaintable_area = walls_m2 * percent_unpaintable / 100
total_area = walls_m2 - unpaintable_area
painted_m2 = 0

while True:
    litre_paint = input()
    if litre_paint == "Tired!":
        progress = total_area - painted_m2
        print(f"{math.ceil(progress)} quadratic m left.")
        quit()
    painted_m2 += int(litre_paint)
    if painted_m2 > total_area:
        print(f"All walls are painted and you have {math.ceil(painted_m2 - total_area)} l paint left!")
        break
    elif painted_m2 == total_area:
        print("All walls are painted! Great job, Pesho!")
        break

