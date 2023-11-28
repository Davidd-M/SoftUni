animals = input()
animals = animals.split(', ')
i = 0
for animal in animals:
    i += 1
    if animal == 'sheep':
        continue
    elif animal == 'wolf':
        if len(animals) - i == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(animals) - i}! You are about to be eaten by a wolf!")
            break
