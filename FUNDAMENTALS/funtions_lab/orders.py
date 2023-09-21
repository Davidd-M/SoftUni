product = input()
quantity = int(input())


def order(product, quantity):
    price = 0
    if product == "coffee":
        price += quantity * 1.50
    elif product == "coke":
        price += quantity * 1.40
    elif product == "water":
        price += quantity * 1.00
    elif product == "snacks":
        price += quantity * 2.00
    return price

price = order(product, quantity)
print(f'{price:.2f}')