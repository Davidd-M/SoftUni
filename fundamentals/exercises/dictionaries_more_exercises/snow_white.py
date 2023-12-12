dwarfs = {}
colors = {}

while True:
    line = input()
    if line == "Once upon a time":
        break
    dwarf_name, dwarf_hat_color, dwarf_physics = line.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    ID = dwarf_name + ":" + dwarf_hat_color
    if ID not in dwarfs:
        if dwarf_hat_color not in colors:
            colors[dwarf_hat_color] = 1
        else:
            colors[dwarf_hat_color] += 1
        dwarfs[ID] = [0, dwarf_hat_color]
    dwarfs[ID][0] = max([dwarfs[ID][0], dwarf_physics])

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
for key, value in sorted_dwarfs.items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")
