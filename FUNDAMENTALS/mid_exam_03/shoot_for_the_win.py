targets_list = list(map(int, input().split()))
shot_targets = 0

while True:
    index = input()
    if index == "End":
        targets_list = [str(x) for x in targets_list]
        print(f'Shot targets: {shot_targets} -> ' + " ".join(targets_list))
        break
    index = int(index)
    if index >= len(targets_list):
        continue
    current_target = 0
    if targets_list[index] != -1:
        current_target = targets_list[index]
        targets_list[index] = -1
        shot_targets += 1

    # Reduce or Increase the other targets which are not shot
    for i, target in enumerate(targets_list):
        if target > current_target:
            targets_list[i] -= current_target
        else:
            if target <= current_target and target != -1:
                targets_list[i] += current_target



