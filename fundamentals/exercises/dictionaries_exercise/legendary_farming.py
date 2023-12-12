materials = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk = {}
legendary_obtained = False

while True:
    line = input().split()
    for i in range(0, len(line), 2):
        v, k = int(line[i]), line[i + 1].lower()
        if k in key_materials.keys():
            # if k not in materials:
            #     materials[k] = 0
            materials[k] += v
            if materials[k] >= 250:
                legendary_obtained = True
                break
        else:
            if k not in junk:
                junk[k] = 0
            junk[k] += v
    if legendary_obtained:
        break
for k, v in materials.items():
    if v >= 250:
        print(f"{key_materials[k]} obtained!")
        materials[k] -= 250
        for k, v in materials.items():
            print(f"{k}: {v}")
        for k, v in junk.items():
            print(f"{k}: {v}")
