def strike_func(list_targets, index, radius):
    try:
        if index - radius < 0:
            raise IndexError
        elif index + radius >= len(list_targets):
            raise IndexError
        start_index = index - radius
        end_index = index + radius
        list_targets[start_index:end_index + 1] = []
    except IndexError:
        print("Strike missed!")
    return list_targets


def shoot_func(list_targets, index, power):
    if 0 <= index < len(list_targets):
        list_targets[index] -= power
        if list_targets[index] <= 0:
            list_targets.pop(index)
    return list_targets


def add_func(list_targets, index, value):
    if len(list_targets) > index >= 0:
        list_targets.insert(index, value)
    else:
        print("Invalid placement!")
    return list_targets


sequence_targets = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "End":
        print("|".join(list(map(str, sequence_targets))))
        break
    elif command[0] == "Shoot":
        sequence_targets = shoot_func(sequence_targets, int(command[1]), int(command[2]))
    elif command[0] == "Add":
        sequence_targets = add_func(sequence_targets, int(command[1]), int(command[2]))
    elif command[0] == "Strike":
        sequence_targets = strike_func(sequence_targets, int(command[1]), int(command[2]))
