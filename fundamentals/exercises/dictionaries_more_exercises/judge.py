contests_dict = {}

while True:
    line = input()
    if line == "no more time":
        break
    username, contest, points = line.split(" -> ")
    points = int(points)
    if contest not in contests_dict.keys():
        contests_dict[contest] = [username, points]
        continue
    if username not in contests_dict[contest]:
        contests_dict[contest].append(username)
        contests_dict[contest].append(points)
    else:
        list_to_iterate = contests_dict[contest]
        for i in range(0, len(list_to_iterate), 2):
            if username == list_to_iterate[i]:
                if points > list_to_iterate[i + 1]:
                    contests_dict[contest][i + 1] = points
#print(contests_dict)
standings_dict = {}
for current_contest, participants_list in contests_dict.items():
    print(f"{current_contest}: {len(contests_dict[current_contest]) // 2} participants")
    points_sorted_dict = {}
    for i in range(0, len(participants_list), 2):
        name = participants_list[i]
        score = participants_list[i + 1]
        points_sorted_dict[name] = score
    points_sorted_dict = dict(sorted(points_sorted_dict.items(), key=lambda item: (-item[1], item[0])))
    place = 0
    for name, points in points_sorted_dict.items():
        if name not in standings_dict:
            standings_dict[name] = 0
        standings_dict[name] += points
        place += 1
        print(f"{place}. {name} <::> {points}")
print("Individual standings:")
# print every participant ordered by total points in descending order, and then by alphabetical order
standings_dict = dict(sorted(standings_dict.items(), key=lambda item: (-item[1], item[0])))
#print(standings_dict)
standing = 0
for person, points in standings_dict.items():
    standing += 1
    print(f"{standing}. {person} -> {points}")
