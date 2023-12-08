num_people = int(input())
season = input()
price = 0
if num_people <= 5:
    if season == 'spring':
        price = 50.00
    elif season == 'summer':
        price = 48.50
    elif season == 'autumn':
        price = 60.00
    elif season == 'winter':
        price = 86.00
elif num_people > 5:
    if season == 'spring':
        price = 48.00
    elif season == 'summer':
        price = 45.00
    elif season == 'autumn':
        price = 49.50
    elif season == 'winter':
        price = 85.00
total_price = price * num_people
if season == 'summer':
    total_price *= 0.85
elif season == 'winter':
    total_price *= 1.08
print(f'{total_price:.2f} leva.')
