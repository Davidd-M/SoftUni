train = [0] * int(input())

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    if command[0] == "add":
        train[len(train) - 1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train[int(command[1])] -= int(command[2])
print(train)
