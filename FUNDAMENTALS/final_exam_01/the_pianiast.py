def check_for_piece(piece_list, piece):
    for index in range(len(piece_list)):
        if piece == piece_list[index][0]:
            return True
    return False


number_of_pieces = int(input())
pieces_list = []

for _ in range(number_of_pieces):
    pieces_list.append(input().split("|"))
while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    elif command[0] == "Add":
        if not check_for_piece(pieces_list, command[1]):
            pieces_list.append([command[1], command[2], command[3]])
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{command[1]} is already in the collection!")
    elif command[0] == "Remove":
        if check_for_piece(pieces_list, command[1]):
            for index in range(len(pieces_list)):
                if command[1] == pieces_list[index][0]:
                    pieces_list.pop(index)
                    print(f"Successfully removed {command[1]}!")
                    break
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        if check_for_piece(pieces_list, command[1]):
            for index in range(len(pieces_list)):
                if command[1] == pieces_list[index][0]:
                    pieces_list[index].pop(2)
                    pieces_list[index].append(command[2])
                    print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

for current_list in pieces_list:
    print(f"{current_list[0]} -> Composer: {current_list[1]}, Key: {current_list[2]}")