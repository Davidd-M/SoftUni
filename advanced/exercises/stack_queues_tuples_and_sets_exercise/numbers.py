sequence1 = set(map(int, input().split()))
sequence2 = set(map(int, input().split()))

for _ in range(int(input())):
    command = input()
    if "Add First" in command:
        nums = map(int, command[9:].split())
        sequence1.update(nums)
    elif "Add Second" in command:
        nums = map(int, command[10:].split())
        sequence2.update(nums)
    elif "Remove First" in command:
        nums = map(int, command[12:].split())
        sequence1.difference_update(nums)
    elif "Remove Second" in command:
        nums = map(int, command[13:].split())
        sequence2.difference_update(nums)
    elif "Check Subset" in command:
        if sequence1.issubset(sequence2) or sequence2.issubset(sequence1):
            print("True")
        else:
            print("False")

print(', '.join(map(str, sorted(sequence1))))
print(', '.join(map(str, sorted(sequence2))))
