def last_func(list_to_check, count, even_or_odd):
    if count > len(list_to_check):
        print("Invalid count")
        return
    list_to_print = []
    if even_or_odd == "even":
        for number in list_to_check[::-1]:
            if number % 2 == 0:
                list_to_print.append(number)
    elif even_or_odd == 'odd':
        for number in list_to_check[::-1]:
            if number % 2 != 0:
                list_to_print.append(number)
    print(list_to_print[:count])


def first_func(list_to_check, count, even_or_odd):
    if count > len(list_to_check):
        print("Invalid count")
        return
    list_to_print = []
    if even_or_odd == "even":
        for number in list_to_check:
            if number % 2 == 0:
                list_to_print.append(number)
    elif even_or_odd == 'odd':
        for number in list_to_check:
            if number % 2 != 0:
                list_to_print.append(number)
    print(list_to_print[:count])


def min_func(list_to_check, even_or_odd):
    min_index = None
    if even_or_odd == "even":
        evens_list = sorted([x for x in list_to_check if x % 2 == 0])
        if evens_list:
            min_number = min(evens_list)
            min_index = len(list_to_check) - 1 - list_to_check[::-1].index(min_number)
    else:
        odds_list = sorted([int(x) for x in list_to_check if x % 2 != 0])
        if odds_list:
            min_number = min(odds_list)
            min_index = len(list_to_check) - 1 - list_to_check[::-1].index(min_number)
    if min_index is not None:
        return min_index
    return "No matches"


def max_func(list_to_check, even_or_odd):
    max_index = None
    if even_or_odd == "even":
        evens_list = sorted([x for x in list_to_check if x % 2 == 0])
        if evens_list:
            max_number = max(evens_list)
            max_index = len(list_to_check) - 1 - list_to_check[::-1].index(max_number)
    else:
        odds_list = sorted([x for x in list_to_check if x % 2 != 0])
        if odds_list:
            max_number = max(odds_list)
            max_index = len(list_to_check) - 1 - list_to_check[::-1].index(max_number)
    if max_index is not None:
        return max_index
    return "No matches"


def exchange_func(list_to_split, index_to_slit):
    if -len(list_to_split) < index_to_slit < len(list_to_split):
        left = list_to_split[:index_to_slit + 1]
        right = list_to_split[index_to_slit + 1:]
        list_to_split = right + left
    else:
        print("Invalid index")
    return list_to_split


list_to_manipulate = list(map(int, input().split()))

while True:
    command = input()
    if command == 'end':
        print(list_to_manipulate)
        break
    command = command.split()
    if command[0] == "exchange":
        list_to_manipulate = exchange_func(list_to_manipulate, int(command[1]))
    elif command[0] == 'max':  # even or odd
        print(max_func(list_to_manipulate, command[1]))
    elif command[0] == 'min':
        print(min_func(list_to_manipulate, command[1]))
    elif command[0] == 'first':
        first_func(list_to_manipulate, int(command[1]), command[2])
    elif command[0] == 'last':
        last_func(list_to_manipulate, int(command[1]), command[2])
