def health_func(heroes, hero_name, health_amount):
    if heroes[hero_name]['health'] + health_amount > 100:
        print(f"{hero_name} healed for {100 - heroes[hero_name]['health']} HP!")
        heroes[hero_name]['health'] = 100
    else:
        heroes[hero_name]['health'] += health_amount
        print(f"{hero_name} healed for {health_amount} HP!")

    return heroes


def mana_func(heroes, hero_name, mana_amount):
    if heroes[hero_name]['mana'] + mana_amount > 200:
        print(f"{hero_name} recharged for {200 - heroes[hero_name]['mana']} MP!")
        heroes[hero_name]['mana'] = 200
    else:
        heroes[hero_name]['mana'] += mana_amount
        print(f"{hero_name} recharged for {mana_amount} MP!")
    return heroes


n = int(input())
heroes_dict = {}

for _ in range(n):
    hero_name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    heroes_dict[hero_name] = {"health": hp, "mana": mp}

while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    hero_name = command[1]
    if command[0] == "CastSpell":
        mana_needed = int(command[2])
        if heroes_dict[hero_name]["mana"] >= mana_needed:
            heroes_dict[hero_name]["mana"] -= mana_needed
            print(f"{hero_name} has successfully cast {command[3]} and now has {heroes_dict[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {command[3]}!")
    elif command[0] == "TakeDamage":
        damage = int(command[2])
        heroes_dict[hero_name]["health"] -= damage
        if not heroes_dict[hero_name]["health"] <= 0:
            print(f"{hero_name} was hit for {damage} HP by {command[3]} and now has {heroes_dict[hero_name]['health']} HP left!")
        else:
            print(f"{hero_name} has been killed by {command[3]}!")
            del heroes_dict[hero_name]
    elif command[0] == "Recharge":
        mana_amount = int(command[2])
        heroes_dict = mana_func(heroes_dict, hero_name, mana_amount)
    elif command[0] == "Heal":
        health_amount = int(command[2])
        heroes_dict = health_func(heroes_dict, hero_name, health_amount)

for hero, attributes in heroes_dict.items():
    health, mana = attributes['health'], attributes['mana']
    print(f"{hero}")
    print(f"  HP: {health}")
    print(f"  MP: {mana}")
