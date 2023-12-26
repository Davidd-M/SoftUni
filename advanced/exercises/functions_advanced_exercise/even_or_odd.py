def even_odd(*args):
    my_list = list(args)
    command = my_list.pop()
    if command == "even":
        my_list = [int(x) for x in my_list if int(x) % 2 == 0]
    else:
        my_list = [int(x) for x in my_list if int(x) % 2 != 0]
    return my_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))