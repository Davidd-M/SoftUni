command = input()
products = {}

while command != "statistics":
    product, value = command.split(": ")
    if product not in products.keys():
        products[product] = int(value)
    else:
        products[product] += int(value)
    command = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")