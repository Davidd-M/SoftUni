def binary_search(inp_list, target):
    start = 0
    end = len(inp_list) - 1

    while start <= end:
        search_index = (end + start) // 2
        if inp_list[search_index] < target:
            start = search_index + 1
        elif inp_list[search_index] > target:
            end = search_index - 1
        elif inp_list[search_index] == target:
            return search_index
    else:
        return "Target not found"


#should be sorted list
my_list = list(int(x) for x in input().split(", "))
my_target = int(input())
result = binary_search(my_list, my_target)
print(f"Result: {result}")
