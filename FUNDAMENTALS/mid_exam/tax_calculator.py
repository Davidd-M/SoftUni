def family_func(years_to_pay, kilometers_travelled):
    tax = kilometers_travelled // 3000 * 12 + (50 - years_to_pay * 5)
    print(f"A family car will pay {tax:.2f} euros in taxes.")
    return tax


vehicles = input().split(">>")
tax_collected = 0
tax = 0

for vehicle_data in vehicles:
    car_type, years, kilometers = vehicle_data.split()
    if car_type == "family":
        tax_collected += family_func(int(years), int(kilometers))
    elif car_type == 'heavyDuty':
        tax = (int(kilometers) // 9000 * 14 + (80 - int(years) * 8))
        tax_collected += tax
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
    elif car_type == 'sports':
        tax = (int(kilometers) // 2000 * 18 + (100 - int(years) * 9))
        tax_collected += tax
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")
print(f"The National Revenue Agency will collect {tax_collected:.2f} euros in taxes.")