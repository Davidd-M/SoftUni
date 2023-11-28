import re

furniture_bought = []
total_cost = 0
pattern = r">>([A-Z{1}a-z]+)<<([/d+\.?\d]+)!([\d]+)"

while True:
    command = input()
    if command == "Purchase":
        break
    result = re.search(pattern, command)
    if result:
        furniture = result[1]
        price = result[2]
        quantity = result[3]
        total_cost += float(price) * int(quantity)
        furniture_bought.append(furniture)

print("Bought furniture:")
for current_furniture in furniture_bought:
    print(current_furniture)
print(f"Total money spend: {total_cost:.2f}")