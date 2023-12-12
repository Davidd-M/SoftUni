def is_valid_index(check_string, check_index):
    if 0 <= int(check_index) < len(check_string):
        return True
    return False


initial_string = input()

while True:
    command = input().split(":")
    if command[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {initial_string}")
        break
    elif command[0] == "Add Stop":
        index, stop = int(command[1]), command[2]
        if is_valid_index(initial_string, index):
            left_part = initial_string[:index]
            right_part = initial_string[index:]
            initial_string = left_part + stop + right_part
        print(initial_string)
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if is_valid_index(initial_string, start_index) and is_valid_index(initial_string, end_index):
            initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
        print(initial_string)
    elif command[0] == "Switch":
        if command[1] in initial_string:
            initial_string = initial_string.replace(command[1], command[2])
        print(initial_string)

