def move_func(some_list, letters_to_move):
    some_list = some_list[letters_to_move:] + some_list[:letters_to_move]
    return some_list


input_list = list(input())

while True:
    command = input().split("|")
    if command[0] == "Decode":
        print(f"The decrypted message is: {''.join(input_list)}")
        break
    elif command[0] == "Move":
        input_list = move_func(input_list, int(command[1]))
    elif command[0] == "Insert":
        # input_list.insert(int(command[1]), command[2]) # DOESN'T WORK IF GIVEN STR WITH MULTIPLE CHARS
        input_list = f"{''.join(input_list)}"
        new_index, value = int(command[1]), command[2]
        input_list = input_list[:new_index] + value + input_list[new_index:]
        input_list = list(input_list)
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        for index in range(len(input_list)):
            if input_list[index] == substring:
                input_list[index] = replacement
