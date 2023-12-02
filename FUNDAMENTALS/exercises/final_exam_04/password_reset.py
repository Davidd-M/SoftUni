password = input()

while True:
    command = input().split()
    if command[0] == "Done":
        print(f"Your password is: {password}")
        break
    elif command[0] == "TakeOdd":
        password = password[1::2]
        print(password)
    elif command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        substring = password[index:index + length]
        password = password.replace(substring, '', 1)
        print(password)
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")