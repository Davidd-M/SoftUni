input_list = input().split(", ")
check_list = input()

matches_list = [x for x in input_list if x in check_list]
print(matches_list)