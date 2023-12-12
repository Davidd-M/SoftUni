notes = [0] * 10

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)
result = [x for x in notes if x != 0]
print(result)
