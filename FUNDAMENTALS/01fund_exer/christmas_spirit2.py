quantity = int(input())
days = int(input())

ornament_set_price = 2
ornament_set_points = 5

tree_skirt_price = 5
tree_skirt_points = 3

tree_garland_price = 3
tree_garland_points = 10

tree_lights_price = 15
tree_lights_points = 17
price = 0
points = 0
days_passed = 0
while True:
    days_passed += 1
    if days_passed > days:
        break
    else:
        if days_passed % 11 == 0:
            quantity += 2
        if days_passed % 3 == 0 and days_passed % 5 == 0:
            price += (tree_skirt_price + tree_garland_price) * quantity
            points += tree_skirt_points + tree_garland_points
            price += tree_lights_price * quantity
            points += tree_lights_points
            points += 30
        if days_passed % 2 == 0:
            price += ornament_set_price * quantity
            points += ornament_set_points
            if days_passed % 3 == 0 and not days_passed % 5 == 0:
                price += (tree_skirt_price + tree_garland_price) * quantity
                points += tree_skirt_points + tree_garland_points
        elif days_passed % 3 == 0 and not days_passed % 5 == 0:
            price += (tree_skirt_price + tree_garland_price) * quantity
            points += tree_skirt_points + tree_garland_points
        if days_passed % 5 == 0 and not days_passed % 3 == 0:
            price += tree_lights_price * quantity
            points += tree_lights_points
        if days_passed % 10 == 0:
            points -= 20
            price += tree_skirt_price + tree_garland_price + tree_lights_price
        #print(f'{days_passed}day and {points} points and {price} price')
days_passed -= 1
if days_passed % 10 == 0:
    points -= 30
print(f"Total cost: {price}")
print(f"Total spirit: {points}")
