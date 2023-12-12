pokemon_distances = list(map(int, input().split()))
removed_items = 0
while pokemon_distances:
    current_index = int(input())
    if current_index < 0:
        removed_element = pokemon_distances[0]
        removed_items += removed_element
        pokemon_distances.pop(0)
        last_item = pokemon_distances[-1]
        pokemon_distances.insert(0, last_item)
    elif current_index >= len(pokemon_distances):
        removed_element = pokemon_distances[-1]
        removed_items += removed_element
        pokemon_distances.pop()
        first_item = pokemon_distances[0]
        pokemon_distances.insert(len(pokemon_distances), first_item)
    else:
        removed_element = pokemon_distances[current_index]
        removed_items += removed_element
        pokemon_distances.pop(current_index)

    for i, pokemon_dist in enumerate(pokemon_distances):
        if pokemon_dist <= removed_element:
            pokemon_distances[i] += removed_element
        else:
            pokemon_distances[i] -= removed_element

print(removed_items)
