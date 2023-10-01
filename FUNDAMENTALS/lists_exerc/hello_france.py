ticket = 150
list_with_items = input().split("|")
budget = float(input())
original_budget = budget
prices_list = []
profit = 0

for item in list_with_items:
    current_item, price = item.split("->")
    price = float(price)
    if current_item == "Clothes":
        if budget >= price <= 50.00:
            budget -= price
            prices_list.append(price * 1.4)
    elif current_item == "Shoes":
        if budget >= price <= 35.00:
            budget -= price
            prices_list.append(price * 1.4)
    elif current_item == "Accessories":
        if budget >= price <= 20.50:
            budget -= price
            prices_list.append(price * 1.4)
profit = (sum(prices_list) + budget) - original_budget
formatted_prices = [f"{price:.2f}" for price in prices_list]
print(*formatted_prices)
print(f"Profit: {profit:.2f}")
if sum(prices_list) + budget >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
