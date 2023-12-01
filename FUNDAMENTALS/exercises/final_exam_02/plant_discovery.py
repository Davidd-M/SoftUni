n = int(input())
plants_dict = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants_dict[plant] = [int(rarity)]

while True:
    command = input().split(": ")
    if command[0] == "Exhibition":
        break
    if command[0] == "Rate":
        plant, rating = command[1].split(" - ")
        if plant not in plants_dict.keys():
            print("error")
            continue
        plants_dict[plant].append(int(rating))
    elif command[0] == "Update":
        plant, new_rarity = command[1].split(" - ")
        if plant not in plants_dict.keys():
            print("error")
            continue
        plants_dict[plant][0] = int(new_rarity)
    elif command[0] == "Reset":
        plant = command[1]
        if plant not in plants_dict.keys():
            print("error")
            continue
        plants_dict[plant] = [plants_dict[plant][0]]

print("Plants for the exhibition:")
for plant, values in plants_dict.items():
    print(f"- {plant}; Rarity: {values.pop(0)}; Rating: {(sum(values) / len(values) if values else 0):.2f}")