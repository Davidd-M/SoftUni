deck = input().split()
faro_shuffles = int(input())

# Append the first and last cards to the shuffled_deck list
shuffled_deck = [deck[0], deck[-1]]

for _ in range(faro_shuffles):
    half_length = len(deck) // 2
    list1 = deck[:half_length]  # Fixed the indexing here
    list2 = deck[half_length:]  # Fixed the indexing here

    shuffled_deck = []

    for i in range(half_length):
        shuffled_deck.append(list1[i])
        shuffled_deck.append(list2[i])

    deck = shuffled_deck

# Append the last card to the shuffled_deck list
shuffled_deck.append(deck[-1])

print(shuffled_deck)
