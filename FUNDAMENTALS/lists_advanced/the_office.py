happiness_list = input().split()
factor = int(input())

happiness_list_by_factor = [int(x) * 3 for x in happiness_list]
average_happiness = sum(happiness_list_by_factor) / len(happiness_list_by_factor)
happy_employees = len([x for x in happiness_list_by_factor if int(x) >= average_happiness])
if happy_employees >= len(happiness_list) // 2:
    print(f"Score: {happy_employees}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(happiness_list)}. Employees are not happy!")