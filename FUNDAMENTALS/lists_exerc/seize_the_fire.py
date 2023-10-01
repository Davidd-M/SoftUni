type_of_fire = input().split("#")
water_amount = int(input())
effort = 0
fire_put_out = 0

print("Cells:")
for fire in type_of_fire:
    if fire[0] == "H":
        if 81 <= int(fire[7::]) <= 125 and int(fire[7::]) <= water_amount:
            water_amount -= int(fire[7::])
            effort += int(fire[7::]) * 0.25
            fire_put_out += int(fire[7::])
            print(' - ' + fire[7::])
    elif fire[0] == "M":
        if 51 <= int(fire[9::]) <= 80 and int(fire[9::]) <= water_amount:
            water_amount -= int(fire[9::])
            effort += int(fire[9::]) * 0.25
            fire_put_out += int(fire[9::])
            print(' - ' + fire[9::])
    elif fire[0] == "L":
        if 1 <= int(fire[6::]) <= 50 and int(fire[6::]) <= water_amount:
            water_amount -= int(fire[6::])
            effort += int(fire[6::]) * 0.25
            fire_put_out += int(fire[6::])
            print(" - " + fire[6::])
    else:
        continue
    if water_amount <= 0:
        break
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_put_out}")
