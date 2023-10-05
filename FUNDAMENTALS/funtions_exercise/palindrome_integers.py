input_ints = input().split(", ")


def palindrome(ints_list):
    checked_list = []
    for numb in input_ints:
        reversed_num = numb[::-1]
        if numb == reversed_num:
            checked_list.append(True)
        else:
            checked_list.append(False)
    return checked_list


palindrome_list = palindrome(input_ints)
for i in palindrome_list:
    print(i)
