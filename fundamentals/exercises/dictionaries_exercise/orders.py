products = {}

while True:
    command = input()
    if command == "buy":
        break
    name, price, quantity = command.split()
    if name not in products.keys():
        products[name] = [float(price), int(quantity)]
    else:
        products[name][0] = float(price)
        products[name][1] += int(quantity)

for product_name, v in products.items():
    total_price = v[0] * v[1]
    print(f"{product_name} -> {total_price:.2f}")
