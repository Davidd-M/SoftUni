ints_list = list(map(int, input().split()))

average_value = sum(ints_list) / len(ints_list)

above_average_ints_list = [x for x in ints_list if x > average_value]

if above_average_ints_list:
    above_average_ints_list = sorted(above_average_ints_list, reverse=True)
    if len(above_average_ints_list) > 5:
        above_average_ints_list = above_average_ints_list[0:5]
        print(*above_average_ints_list)
    else:
        print(*above_average_ints_list)
else:
    print("No")
