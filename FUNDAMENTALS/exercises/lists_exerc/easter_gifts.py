gifts = input().split()

while True:
    command = input().split()
    if command[0] == "No":
        break
    elif command[0] == "OutOfStock":
        if command[1] in gifts:
            for i, word in enumerate(gifts):
                if command[1] == word:
                    gifts[i] = "None"
    #If the index is valid, replace the gift on the given index with the given gift.
    elif command[0] == "Required":
        if 0 <= int(command[2]) <= int(len(gifts) - 1):
            gifts[int(command[2])] = command[1]
        else:
            continue
    #Replace the value of your last gift with this one.
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))

