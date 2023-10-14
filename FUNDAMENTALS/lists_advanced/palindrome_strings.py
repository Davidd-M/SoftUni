strings_list = input().split()
palindrome_to_find = input()


def palindrome_checker(_list, _str):
    palindrome_list = [x for x in strings_list if x == x[::-1]]
    print(palindrome_list)
    times_found = palindrome_list.count(palindrome_to_find)
    print(f"Found palindrome {times_found} times")


palindrome_checker(strings_list, palindrome_to_find)
