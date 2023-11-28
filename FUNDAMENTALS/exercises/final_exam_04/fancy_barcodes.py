import re

number_of_barcodes = int(input())
barcodes_list = []
product_group = 00
pattern = r"@[#]+[A-Z][A-Za-z0-9]{4,}[A-Z]@[#]+"
product_group_pattern = r"\d"

for _ in range(number_of_barcodes):
    barcodes_list.append(input())

for barcode in barcodes_list:
    result = re.findall(pattern, barcode)
    if result:
        product_group_result = re.findall(product_group_pattern, barcode)
        product_group = ''.join(product_group_result)
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")

