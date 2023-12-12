followers_dict = {}

while True:
    command = input().split(": ")
    if command[0] == "Log out":
        break
    elif command[0] == "New follower":
        username = command[1]
        if username not in followers_dict.keys():
            followers_dict[username] = {"likes": 0, "comments": 0}
    elif command[0] == "Like":
        username, like = command[1], int(command[2])
        if username in followers_dict.keys():
            followers_dict[username]["likes"] += like
        else:
            followers_dict[username] = {"likes": like, "comments": 0}
    elif command[0] == "Comment":
        username = command[1]
        if username in followers_dict.keys():
            followers_dict[username]["comments"] += 1
        else:
            followers_dict[username] = {"likes": 0, "comments": 1}
    elif command[0] == "Blocked":
        username = command[1]
        if username in followers_dict:
            del followers_dict[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers_dict.keys())} followers")
for follower, attributes in followers_dict.items():
    likes, comments = int(attributes["likes"]), int(attributes["comments"])
    print(f"{follower}: {likes + comments}")