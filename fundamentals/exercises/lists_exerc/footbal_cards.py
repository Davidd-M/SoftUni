team_A = [1,2,3,4,5,6,7,8,9,10,11]
team_B = [1,2,3,4,5,6,7,8,9,10,11]
card_inp = input()
cards_list = card_inp.split( )
for card in cards_list:
    number_player = int(card[2:])
    try:
        if card[0] == 'A':
            team_A.remove(number_player)
        elif card[0] == 'B':
            team_B.remove(number_player)
        if len(team_A) < 7 or len(team_B) < 7:
            players_A = len(team_A)
            players_B = len(team_B)
            print(f"Team A - {players_A}; Team B - {players_B}")
            print("Game was terminated")
            quit()
    except ValueError:
        continue
players_A = len(team_A)
players_B = len(team_B)
print(f"Team A - {players_A}; Team B - {players_B}")