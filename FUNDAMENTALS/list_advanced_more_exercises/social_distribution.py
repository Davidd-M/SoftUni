wealth_list = list(map(int, input().split(", ")))
minimum_wealth = int(input())
total_people = len(wealth_list)


for person in wealth_list:
    if min(wealth_list) < minimum_wealth:
        max_index = wealth_list.index(max(wealth_list))
        min_index = wealth_list.index(min(wealth_list))
        wealth_list[max_index] -= (minimum_wealth - min(wealth_list))
        wealth_list[min_index] = minimum_wealth
if min(wealth_list) < minimum_wealth:
    print('No equal distribution possible')
else:
    print(wealth_list)
