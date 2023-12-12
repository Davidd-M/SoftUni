players_dict = {}

while True:
    line = input()
    if line == "Season end":
        break
    if " -> " in line:
        player, position, skill = line.split(" -> ")
        skill = int(skill)
        if player not in players_dict.keys():
            players_dict[player] = [position, skill]
        elif position not in players_dict[player]:
            players_dict[player].append(position)
            players_dict[player].append(skill)
        # IF position is present for the player
        elif position in players_dict[player]:
            # Check if he has updated his skill for this position
            skill_index = players_dict[player].index(position) + 1
            if players_dict[player][skill_index] < skill:
                players_dict[player][skill_index] = skill

    elif " vs " in line:
        player1, player2 = line.split(" vs ")
        # if there isn't one of the players
        if player2 not in players_dict.keys() or player1 not in players_dict.keys():
            continue
        # if they have at least one position in common
        # for every position in player1 list
        players_1_points = 0
        players_2_points = 0
        for i in range(0, len(players_dict[player1]), 2):
            position = players_dict[player1][i]
            # if they have matching positions
            if position in players_dict[player2]:
                total_skill_points_1 = sum([int(x) for x in players_dict[player1][1::2]])
                total_skill_points_2 = sum([int(x) for x in players_dict[player2][1::2]])
                # check the outcome of the duel
                if total_skill_points_1 > total_skill_points_2:
                    players_1_points += total_skill_points_1
                elif total_skill_points_2 > total_skill_points_1:
                    players_2_points += total_skill_points_2
                # if it's a draw for the current position
                else:
                    pass
        # check who won on more positions
        if players_1_points > players_2_points:
            players_dict.pop(player2)
        elif players_2_points > players_1_points:
            players_dict.pop(player1)
        # if the whole duel is a draw
        # if they don't have any positions in common
        else:
            pass

players_skill_dict = {}
# order players by skill in descending order
for current_player, list_with_positions_and_skill in players_dict.items():
    if current_player not in players_skill_dict:
        players_skill_dict[current_player] = 0
    for i in range(1, len(list_with_positions_and_skill), 2):
        current_points = list_with_positions_and_skill[i]
        players_skill_dict[current_player] += int(current_points)
players_skill_dict = dict(sorted(players_skill_dict.items(), key=lambda item: (-item[1], item[0])))

# print all the player sorted by highest total skill
for person, total_points in players_skill_dict.items():
    print(f"{person}: {total_points} skill")
    pos_and_skill_dict = {players_dict[person][i]: players_dict[person][i + 1] for i in
                          range(0, len(players_dict[person]), 2)}
    sorted_pos_and_skill_dict = dict(sorted(pos_and_skill_dict.items(), key=lambda item: (-item[1], item[0])))
    # print all the current players positions and skill
    for current_position, current_points in sorted_pos_and_skill_dict.items():
        print(f"- {current_position} <::> {current_points}")
