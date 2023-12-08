fruit = input()
size = input()
num_sets = int(input())

price = 0

if size == 'small':
    size = 2
    if fruit == 'Watermelon':
        price = 56
    elif fruit == 'Mango':
        price = 36.66
    elif fruit == 'Pineapple':
        price = 42.10
    elif fruit == 'Raspberry':
        price = 20
elif size == 'big':
    size = 5
    if fruit == 'Watermelon':
        price = 28.7
    elif fruit == 'Mango':
        price = 19.6
    elif fruit == 'Pineapple':
        price = 24.8
    elif fruit == 'Raspberry':
        price = 15.2

total_price = (num_sets * size) * price

if 1000 >= total_price >= 400:
    total_price -= total_price * 0.15
elif total_price > 1000:
    total_price -= total_price * 0.5

print(f'{total_price:.2f} lv.')

