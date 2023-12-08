money_needed = float(input())
money_available = float(input())
spend_days = 0
total_days = 0
total_money = 0 + money_available
while True:
    action = input()
    total_days += 1
    if action == 'spend':
        spend_days += 1
        if spend_days >= 5:
            print("You can't save the money.")
            print(f"{total_days}")
            break
        amount = float(input())
        total_money -= amount
        if total_money < 0:
            total_money = 0
    elif action == "save":
        spend_days = 0
        amount = float(input())
        total_money += amount
    if money_needed <= total_money:
        print(f"You saved the money for {total_days} days.")
        break
