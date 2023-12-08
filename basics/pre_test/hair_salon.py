target = int(input())
turnover = 0
while True:
    service = input()
    if service == 'closed':
        diff = abs(turnover - target)
        print(f'Target not reached! You need {int(diff)}lv. more.')
        print(f"Earned money: {turnover}lv.")
        break
    elif service == 'haircut':
        type_of_haircut = input()
        if type_of_haircut == 'mens':
            price = 15
            turnover += price
        elif type_of_haircut == 'ladies':
            price = 20
            turnover += price
        elif type_of_haircut == 'kids':
            price = 10
            turnover += price
    elif service == 'color':
        type_of_coloring = input()
        if type_of_coloring == 'touch up':
            price = 20
            turnover += price
        elif type_of_coloring == 'full color':
            price = 30
            turnover += price
    if turnover >= target:
        print("You have reached your target for the day!")
        print(f"Earned money: {turnover}lv.")
        break