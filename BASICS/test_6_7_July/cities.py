city = input()
package_type = input()
vip = input()
days = int(input())

price = 0

if days < 1:
    print("Days must be positive number!")
    quit()
elif days > 7:
    days -= 1
if vip != 'yes' and vip != 'no':
    print("Invalid input!")
if city == 'Bansko' or city == 'Borovets':
    if package_type == 'noEquipment':
        price = 80
        if vip == 'yes':
            price -= price * 0.05
    elif package_type == 'withEquipment':
        price = 100
        if vip == 'yes':
            price -= price * 0.10
if city == 'Varna' or city == 'Burgas':
    if package_type == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price -= price * 0.07
    elif package_type == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price -= price * 0.12

total_price = price * days
if total_price == 0:
    print("Invalid input!")
    quit()
print(f"The price is {total_price:.2f}lv! Have a nice time!")
