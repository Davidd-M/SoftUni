import math

m2_area = int(input())
grape_kg_for_m2 = float(input())
litre_wine_for_sale = int(input())
workers_number = int(input())


total_harvest = grape_kg_for_m2 * m2_area
wine_harvest = total_harvest * 0.4
liters_wine = wine_harvest / 2.5
sale_diff = math.floor(int(abs(litre_wine_for_sale - liters_wine)))
wine_for_worker = math.ceil(int(liters_wine - litre_wine_for_sale) / workers_number)

if liters_wine < litre_wine_for_sale:
    print(f'It will be a tough winter! More {sale_diff} liters wine needed.')
elif liters_wine >= litre_wine_for_sale:
    print(f'Good harvest this year! Total wine: {math.floor(int((liters_wine)))} liters.')
    print(f'{sale_diff} liters left -> {wine_for_worker} liters per person.')