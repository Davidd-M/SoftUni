coffee_type = input()
sugar = input()
num_drinks = int(input())

price = 0

if coffee_type == "Espresso":
    if sugar == 'Without':
        price = 0.9
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.2
elif coffee_type == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.2
    elif sugar == 'Extra':
        price = 1.6
elif coffee_type == 'Tea':
    if sugar == 'Without':
        price = 0.5
    elif sugar == 'Normal':
        price = 0.6
    elif sugar == 'Extra':
        price = 0.7

total_price = price * num_drinks
if sugar == 'Without':
    total_price -= total_price * 0.35
if coffee_type == 'Espresso' and num_drinks >= 5:
    total_price -= total_price * 0.25
if total_price > 15:
    total_price -= total_price * 0.20
print(f"You bought {num_drinks} cups of {coffee_type} for {total_price:.2f} lv.")