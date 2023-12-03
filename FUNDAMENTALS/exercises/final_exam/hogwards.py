spell = input()

while True:
    command = input().split()
    if command[0] == "Abracadabra":
        break
    elif command[0] == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command[0] == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif command[0] == "Illusion":
        index, letter = int(command[1]), command[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif command[0] == "Divination":
        first_substring, second_substring = command[1], command[2]
        spell = spell.replace(first_substring, second_substring)
        print(spell)
    elif command[0] == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
        else:
            print("The spell did not work!")
    else:
        print("The spell did not work!")