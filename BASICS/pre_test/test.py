num_rolls_paper = int(input())
num_rolls_cloth = int(input())
litre_glue = float(input())
discount_percent = int(input())

paper_roll_price = 5.80
cloth_roll_price = 7.20
glue_litre_price = 1.20

paper_roll_price_total = paper_roll_price * num_rolls_paper
cloth_roll_price_total = cloth_roll_price * num_rolls_cloth
glue_litre_price_total = glue_litre_price * litre_glue
total_price = paper_roll_price_total + cloth_roll_price_total + glue_litre_price_total
discounted_price = total_price - ((total_price * discount_percent) / 100)

print(f'{discounted_price:.3f}')