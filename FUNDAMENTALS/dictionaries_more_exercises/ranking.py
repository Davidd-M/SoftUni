valid_contests_and_passwords = {}
saved_submissions = {}

while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    valid_contests_and_passwords[contest] = password

while True:
    line2 = input()
    if line2 == "end of submissions":
        break
    contest, password, username, points = line2.split("=>")
    points = int(points)

    for current_contest, curr_password in valid_contests_and_passwords.items():
        # check if pass and username are valid
        if contest == current_contest and password == curr_password:
            # check if there isn't such contest
            if contest not in saved_submissions.keys():
                saved_submissions[contest] = [username, points]
            # if contest is in already
            elif contest in saved_submissions.keys():
                # if there isn't such user already
                if username not in saved_submissions[contest]:
                    saved_submissions[contest].append(username)
                    saved_submissions[contest].append(points)
                # if there is
                else:
                    points_index = (saved_submissions[contest].index(username)) + 1
                    if saved_submissions[contest][points_index] < points:
                        saved_submissions[contest][points_index] = points

                    # # check for the user and their points
                    # for i, user in enumerate(saved_submissions[contest]):
                    #     # if there is such user
                    #     if username == user:
                    #         # change the points if they are higher, accessing them by index
                    #         if saved_submissions[contest][i + 1] < points:
                    #             saved_submissions[contest][i + 1] = points
#print(saved_submissions)
candidates_dict = {}
# check for best candidate
for list_with_candidates in saved_submissions.values():
    for i in range(0, len(list_with_candidates), 2):
        candidate = list_with_candidates[i]
        points = list_with_candidates[i + 1]
        if candidate not in candidates_dict.keys():
            candidates_dict[candidate] = 0
        candidates_dict[candidate] += points
# sort the dict by points
candidates_dict = dict(sorted(candidates_dict.items(), key=lambda item: item[1], reverse=True))
best_candidate, best_score = next(iter(candidates_dict.items()))
print(f"Best candidate is {best_candidate} with total {best_score} points.")
#candidates_dict = dict(sorted(candidates_dict.items()))
#print(candidates_dict)
candidates_list_sorted = sorted([x for x in candidates_dict.keys()])
#print(candidates_list_sorted)
print("Ranking:")
# Print every person and the courses points
saved_submissions = dict(sorted(saved_submissions.items(), key=lambda item: item[1][1], reverse=True))
#print(saved_submissions)
for person_in_list in candidates_list_sorted:
    print(person_in_list)
    for current_contest, list_with_candidates in saved_submissions.items():
        if person_in_list not in list_with_candidates:
            continue
        else:
            points_index = (saved_submissions[current_contest].index(person_in_list)) + 1
            print(f"#  {current_contest} -> {saved_submissions[current_contest][points_index]}")
