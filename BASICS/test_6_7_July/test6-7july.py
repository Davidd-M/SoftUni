import math

people = int(input())
entrance = float(input())
lounger = float(input())
umbrella = float(input())

total_entrance = people * entrance
total_umbrella = math.ceil((people / 2)) * umbrella
total_lounger = math.ceil((people * 0.75)) * lounger
total_price = total_lounger + total_umbrella + total_entrance

print(f'{total_price:.2f} lv.')