from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
toys = {}

while materials and magic_levels:
    curr_magic_level = magic_levels.popleft()
    cur_material = materials.pop()
    magic_level = cur_material * curr_magic_level
    if magic_level == 150:
        if "Doll" not in toys:
            toys["Doll"] = 0
        toys["Doll"] += 1
    elif magic_level == 250:
        if "Wooden train" not in toys:
            toys["Wooden train"] = 0
        toys["Wooden train"] += 1
    elif magic_level == 300:
        if "Teddy bear" not in toys:
            toys["Teddy bear"] = 0
        toys["Teddy bear"] += 1
    elif magic_level == 400:
        if "Bicycle" not in toys:
            toys["Bicycle"] = 0
        toys["Bicycle"] += 1
    elif magic_level < 0:
        magic_level = cur_material + curr_magic_level
        materials.append(magic_level)
    elif magic_level > 0:
        materials.append(cur_material + 15)
    else:
        if cur_material != 0:
            materials.append(cur_material)
        if curr_magic_level != 0:
            magic_levels.appendleft(curr_magic_level)

if "Doll" in toys and "Wooden train" in toys or "Teddy bear" in toys and "Bicycle" in toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

[print(f"{toy}: {toys[toy]}") for toy in sorted(set(toys))]
