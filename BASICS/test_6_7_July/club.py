wanted_profit = float(input())

profit = 0

while True:
    cocktail = input()
    if cocktail == 'Party!':
        diff = wanted_profit - profit
        print(f"We need {diff:.2f} leva more.")
        break
    num_cocktails = int(input())
    cocktail_price = len(cocktail)
    total_price = cocktail_price * num_cocktails
    if total_price % 2 != 0:
        total_price -= total_price * 0.25
    profit += total_price
    if wanted_profit <= profit:
        print("Target acquired.")
        break

print(f"Club income - {profit:.2f} leva.")