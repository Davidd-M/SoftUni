def last_func(list_to_check, count, even_or_odd):
    if even_or_odd == "even":
        even_list = []
        if count > len(list_to_check):
            print("Invalid count")
        else:
            for index in range(len(list_to_check) - 1, -1, -1):
                if len(even_list) == count:
                    break
                if list_to_check[index] % 2 == 0:
                    even_list.append(list_to_check[index])
            even_list.reverse()
            print(even_list)
    elif even_or_odd == "odd":
        odd_list = []
        if count > len(list_to_check):
            print("Invalid count")
        else:
            for index in range(len(list_to_check) - 1, -1, -1):
                if len(odd_list) == count:
                    break
                if list_to_check[index] % 2 != 0:
                    odd_list.append(list_to_check[index])
            odd_list.reverse()
            print(odd_list)


def first_func(list_to_check, count, even_or_odd):
    if count > len(list_to_check):
        print("Invalid count")
        return
    list_to_print = []
    if even_or_odd == "even":
        for number in list_to_check:
            if number % 2 == 0:
                list_to_print.append(number)
                if len(list_to_print) == count:
                    break
    elif even_or_odd == 'odd':
        for number in list_to_check:
            if number % 2 != 0:
                list_to_print.append(number)
                if len(list_to_print) == count:
                    break
    print(list_to_print)


def min_func(list_to_check, even_or_odd):
    if even_or_odd == "even":
        evens_list = [int(x) for x in list_to_check if x % 2 == 0]
        if evens_list:
            min_number = min(evens_list)
            min_index = -1
            for index in range(len(list_to_check) - 1, -1, -1):
                if list_to_check[index] == min_number:
                    min_index = index
                    break
            if min_index > -1:
                print(min_index)
            else:
                print("No matches")
        else:
            print("No matches")
    elif even_or_odd == "odd":
        odds_list = [int(x) for x in list_to_check if x % 2 != 0]
        if odds_list:
            min_number = min(odds_list)
            min_index = -1
            for index in range(len(list_to_check) - 1, -1, -1):
                if list_to_check[index] == min_number:
                    min_index = index
                    break
            if min_index > -1:
                print(min_index)
            else:
                print("No matches")
        else:
            print("No matches")


def max_func(list_to_check, even_or_odd):
    if even_or_odd == "even":
        evens_list = [int(x) for x in list_to_check if x % 2 == 0]
        if evens_list:
            max_number = max(evens_list)
            max_index = -1
            for index in range(len(list_to_check) - 1, -1, -1):
                if list_to_check[index] == max_number:
                    max_index = index
                    break
            if max_index > -1:
                print(max_index)
            else:
                print("No matches")
        else:
            print("No matches")
    elif even_or_odd == "odd":
        odds_list = [int(x) for x in list_to_check if x % 2 != 0]
        if odds_list:
            max_number = max(odds_list)
            max_index = -1
            for index in range(len(list_to_check) - 1, -1, -1):
                if list_to_check[index] == max_number:
                    max_index = index
                    break
            if max_index > -1:
                print(max_index)
            else:
                print("No matches")
        else:
            print("No matches")


def exchange_func(list_to_split, index_to_slit):
    if 0 <= index_to_slit < len(list_to_split):
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
    elif command[0] == 'max':
        max_func(list_to_manipulate, command[1])
    elif command[0] == 'min':
        min_func(list_to_manipulate, command[1])
    elif command[0] == 'first':
        first_func(list_to_manipulate, int(command[1]), command[2])
    elif command[0] == 'last':
        last_func(list_to_manipulate, int(command[1]), command[2])
