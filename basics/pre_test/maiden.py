maiden_party_price = float(input())
num_love_wishes = int(input())
num_wax_roses = int(input())
num_keychains = int(input())
num_caricatures = int(input())
num_fortunes = int(input())

price_love_wish = 0.60
price_wax_rose = 7.20
price_keychain = 3.60
price_caricature = 18.20
price_fortune = 22
total_price = (price_love_wish * num_love_wishes) + (price_wax_rose * num_wax_roses) + (price_keychain * num_keychains) + (price_caricature * num_caricatures) + (num_fortunes * price_fortune)


if num_love_wishes + num_wax_roses + num_keychains + num_caricatures + num_fortunes >= 25:
    total_price = total_price - (total_price * 0.35)
total_price *= 0.9
diff = abs(total_price - maiden_party_price)
if total_price >= maiden_party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
