def categorize_input(dragon_and_stats, dragons_dict):
    type_dragon, name, damage, health, armor = dragon_and_stats

    if health == "null":
        health = 250
    if damage == "null":
        damage = 45
    if armor == "null":
        armor = 10

    if type_dragon not in dragons_dict:
        dragons_dict[type_dragon] = {}

    dragons_dict[type_dragon].update(
        {name: {"damage": int(damage), "health": int(health), "armor": int(armor)}})

    return dragons_dict


def average_stats_func(stats_dict):
    average_stats_for_type = {"average_health": 0, "average_damage": 0, "average_armor": 0}
    average_health = 0
    average_damage = 0
    average_armor = 0
    dragons = 0

    for name, stats in stats_dict.items():
        dragons += 1
        average_health += stats["health"]
        average_damage += stats["damage"]
        average_armor += stats["armor"]

    average_stats_for_type["average_health"] = average_health / dragons
    average_stats_for_type["average_damage"] = average_damage / dragons
    average_stats_for_type["average_armor"] = average_armor / dragons

    return average_stats_for_type


average_stats = {}
dragon_dict = {}

for _ in range(int(input())):
    dragon_dict = categorize_input(input().split(), dragon_dict)

# print(dragon_dict)

for current_type, current_name_and_stats in dragon_dict.items():
    current_name_and_stats = dict(sorted(current_name_and_stats.items(), key=lambda x: x[0]))
    dragon_dict[current_type] = current_name_and_stats

    average_for_type = average_stats_func(current_name_and_stats)
    average_stats.update({current_type: average_for_type})

# print(average_stats)
# print(dragon_dict)

for current_type, dragons_and_stats in dragon_dict.items():
    average_health = average_stats[current_type]["average_health"]
    average_damage = average_stats[current_type]["average_damage"]
    average_armor = average_stats[current_type]["average_armor"]

    print(f"{current_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for dragon_name, dragon_stats in dragons_and_stats.items():
        curr_damage = dragon_stats["damage"]
        curr_health = dragon_stats["health"]
        curr_armor = dragon_stats["armor"]
        print(f"-{dragon_name} -> damage: {curr_damage}, health: {curr_health}, armor: {curr_armor}")
