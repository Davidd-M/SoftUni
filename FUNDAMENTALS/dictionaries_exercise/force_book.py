sides_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    elif " | " in command:
        force_side, force_user = command.split(" | ")
        if force_side not in sides_dict.keys():
            sides_dict[force_side] = []
        for side, users in sides_dict.items():
            if force_user in users:
                break
        else:
            sides_dict[force_side].append(force_user)
    elif " -> " in command:
        side_changed = False
        force_user, force_side = command.split(" -> ")
        print(f"{force_user} joins the {force_side} side!")
        for side, users_list in sides_dict.items():
            if force_user in users_list:
                users_list.remove(force_user)
                if force_side in sides_dict.keys():
                    sides_dict[force_side].append(force_user)
                else:
                    sides_dict[force_side] = [force_user]
                side_changed = True
                break
        if not side_changed:
            if force_side in sides_dict.keys():
                sides_dict[force_side].append(force_user)
            else:
                sides_dict[force_side] = [force_user]
for force_side, users_list in sides_dict.items():
    if len(users_list) > 0:
        print(f"Side: {force_side}, Members: {len(users_list)}")
        for user in users_list:
            print(f"! {user}")