budget = float(input())
nights = int(input())
price_night = float(input())
percent_additional = int(input())

if nights > 7:
    price_night -= price_night * 0.05

total_price_night = nights * price_night
total_price = total_price_night + (budget * percent_additional / 100)
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
