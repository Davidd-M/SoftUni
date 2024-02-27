def team_lineup(*args):
    my_dict = dict(args)
    new_dict = {}

    for player, country in my_dict.items():
        if country not in new_dict.keys():
            new_dict[country] = []
        new_dict[country].append(player)

    new_dict = dict(sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    print_str = ''

    for country, players in new_dict.items():
        print_str += country + ":\n"
        for player in players:
            print_str += f"  -{player}\n"

    return print_str


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


