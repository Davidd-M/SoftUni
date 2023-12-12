password = input()


def pass_checker(password : str):
    checker = True
    digit_count = 0
    failed_tests = []
    if 6 <= len(password) <= 10:
        pass
    else:
        failed_tests.append("Password must be between 6 and 10 characters")
        checker = False
    for letter in password:
        if letter.isdigit() or letter.isalpha():
            continue
        else:
            failed_tests.append("Password must consist only of letters and digits")
            checker = False
            break
    for letter in password:
        if letter.isdigit():
            digit_count += 1
    if digit_count < 2:
        checker = False
        failed_tests.append("Password must have at least 2 digits")
    if checker == True:
        return checker
    else:
        return failed_tests


if pass_checker(password) == True:
    print("Password is valid")
else:
    for failed_test in pass_checker(password):
        print(failed_test)
