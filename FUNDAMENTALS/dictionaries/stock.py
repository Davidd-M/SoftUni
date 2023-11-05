input_list =input().split()
needed_products = input().split()

products = dict()

for i in range(0, len(input_list), 2):
    key = input_list[i]
    value = input_list[i + 1]
    products[key] = int(value)

for product in needed_products:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
