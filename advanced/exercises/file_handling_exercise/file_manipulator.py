import os

while True:
    command, *info = input().split("-")
    if command == "End":
        break
    elif command == "Create":
        with open(info[0], "w"):
            pass
    elif command == "Add":
        with open(info[0], "a") as file:
            file.write(info[1] + "\n")
    elif command == "Replace":
        try:
            with open(info[0], "r+") as f:
                lines = f.readlines()
                f.seek(0)
                f.truncate()
                for line in lines:
                    line = line.replace(info[1], info[2])
                    f.write(line)

        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove(info[0])
        except FileNotFoundError:
            print("An error occurred")
