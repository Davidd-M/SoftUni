input_names = input().split(", ")


def sorting_names(list_names: list):
    sorted_list = sorted(list_names, key=lambda x: (-len(x), x))
    print(sorted_list)


sorting_names(input_names)
