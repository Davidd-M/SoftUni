prices_list = []
while True:
    part_price = input()
    if part_price == "special":
        if len(prices_list) == 0:
            print('Invalid order!')
            quit()
        price_without_tax = sum(prices_list)
        taxes = (sum(prices_list) * 1.2) - price_without_tax
        price_with_vat = (price_without_tax + taxes) * 0.9
        print("Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_tax:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              "-----------\n"
              f"Total price: {price_with_vat:.2f}$")
        break
    elif part_price == "regular":
        if len(prices_list) == 0:
            print('Invalid order!')
            quit()
        price_without_tax = sum(prices_list)
        price_with_vat = price_without_tax * 1.2
        taxes = price_with_vat - price_without_tax
        print("Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_tax:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              "-----------\n"
              f"Total price: {price_with_vat:.2f}$")
        break
    elif float(part_price) < 0:
        print("Invalid price!")
        continue
    prices_list.append(float(part_price))
