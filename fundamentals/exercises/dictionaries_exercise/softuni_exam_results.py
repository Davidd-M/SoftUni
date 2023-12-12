def ban(a_dict, user: str):
    del a_dict[user]
    return a_dict


unique_langs = {}
results_dict = {}
while True:
    command = input()
    if command == "exam finished":
        break
    elif "-banned" in command:
        username_to_ban = command.split("-")[0]
        results_dict = ban(results_dict, username_to_ban)
        continue
    username, language, points = command.split("-")
    if language not in unique_langs:
        unique_langs[language] = 0
    unique_langs[language] += 1
    points = int(points)
    if username not in results_dict:
        results_dict[username] = [language, points]
    if language not in results_dict[username]:
        results_dict[username].append(language)
        results_dict[username].append(points)
    list_to_iterate = results_dict[username]
    for points_in_list in range(0, len(list_to_iterate), 2):
        if language == list_to_iterate[points_in_list]:
            if points > list_to_iterate[points_in_list + 1]:
                results_dict[username][points_in_list + 1] = points

print("Results:")
for user, data in results_dict.items():
    if user != "banned!":
        print(f"{user} | {data[1]}")
print("Submissions:")
for lang, count in unique_langs.items():
    print(f"{lang} - {count}")
