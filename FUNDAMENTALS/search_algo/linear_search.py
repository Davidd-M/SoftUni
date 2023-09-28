def linear_search(inp_list, target):
    index = -1
    for element in inp_list:
        index += 1
        if element == target:
            target = index
            return target


inp_list = [1, 3, 5, 7, 9, 11]
target = 7
result = linear_search(inp_list, target)
if result != -1:
    print(f"The target element {target} is at index {result}.")
else:
    print(f"The target element {target} was not found in the list.")