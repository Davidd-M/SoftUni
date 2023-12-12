electrons = int(input())
shell = 0
filled_electrons_list = []
while True:
    shell += 1
    diff = electrons - (electrons - (2 * shell ** 2))
    if electrons - (sum(filled_electrons_list) + diff) <= 0:
        filled_electrons_list.append(electrons - sum(filled_electrons_list))
        break
    else:
        asd = electrons - (2 * shell ** 2)
        filled_electrons_list.append(diff)

print(filled_electrons_list)
