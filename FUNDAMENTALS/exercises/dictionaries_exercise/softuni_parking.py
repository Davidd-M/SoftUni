def unregistered_func(users: dict, username: str) -> dict:
    if username not in users.keys():
        print(f"ERROR: user {username} not found")
    else:
        users.pop(username)
        print(f"{username} unregistered successfully")
    return users


def register_func(users: dict, username: str, license_plate: str) -> dict:
    if username in users.keys():
        print(f"ERROR: already registered with plate number {license_plate}")
    else:
        users[username] = license_plate
        print(f"{username} registered {license_plate} successfully")
    return users


n = int(input())
registered = {}

for registration in range(n):
    command = input().split()
    if command[0] == "register":
        registered = register_func(registered, command[1], command[2])
    elif command[0] == "unregister":
        registered = unregistered_func(registered, command[1])

for k, v in registered.items():
    print(f"{k} => {v}")


