
def reverse_func(string_to_change, substring):
    if substring in string_to_change:
        string_to_change = string_to_change.replace(substring, "", 1)
        string_to_change += substring[::-1]
        print(string_to_change)
    else:
        print("error")
    return string_to_change


message = input()

while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break
    elif command[0] == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command[0] == "Reverse":
        message = reverse_func(message, command[1])
    elif command[0] == "ChangeAll":
        message = message.replace(command[1], command[2])
        print(message)

print(f"You have a new text message: {message}")