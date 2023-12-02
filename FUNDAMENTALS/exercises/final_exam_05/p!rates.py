def prosper_func(cities_dict, city, gold_increase):
    if gold_increase < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        cities_dict[city][1] += gold_increase
        print(f"{gold_increase} gold added to the city treasury. {city} now has {cities_dict[city][1]} gold.")
    return cities_dict


def plunder_func(cities_dict, city, killed_ppl, gold_stolen):
    cities_dict[city][0] -= killed_ppl
    cities_dict[city][1] -= gold_stolen
    print(f"{city} plundered! {gold_stolen} gold stolen, {killed_ppl} citizens killed.")
    if cities_dict[city][0] == 0 or cities_dict[city][1] == 0:
        del cities_dict[city]
        print(f"{city} has been wiped off the map!")
    return cities_dict


towns_dict = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break
    else:
        curr_town = command[0]
        curr_people = int(command[1])
        curr_gold = int(command[2])
        if curr_town not in towns_dict.keys():
            towns_dict[curr_town] = [curr_people, curr_gold]
        else:
            towns_dict[curr_town][0] += curr_people
            towns_dict[curr_town][1] += curr_gold


while True:
    line = input().split("=>")
    if line[0] == "End":
        break
    town = line[1]
    gold = int(line[-1])
    if line[0] == "Plunder":
        people = int(line[2])
        towns_dict = plunder_func(towns_dict, town, people, gold)
    elif line[0] == "Prosper":
        towns_dict = prosper_func(towns_dict, town, gold)

if towns_dict:
    print(f"Ahoy, Captain! There are {len(towns_dict.keys())} wealthy settlements to go to:")
    for town_left, (people_left, gold_left) in towns_dict.items():
        print(f"{town_left} -> Population: {people_left} citizens, Gold: {gold_left} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
