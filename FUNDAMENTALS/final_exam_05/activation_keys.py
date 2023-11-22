activation_key = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    elif command[0] == "Contains":
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
        else:
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
        print(activation_key)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
