def valid_func(user):
    valid = True
    for character in username:
        if not (character.isdigit()
                or character.isalpha()
                or "-" == character
                or "_" == character):
            valid = False
            break
    if valid:
        print(username)


usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:  # and " " not in username:
        if valid_func(username):
            print(username)
