days = int(input())
money_total = 0
day_won = 0
for day in range(1, days + 1):
    money_daily = 0
    games_won_daily = 0
    games_lost_daily = 0
    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()
        if result == 'win':
            money = 20
            games_won_daily += 1
            money_daily += money
        else:
            games_lost_daily += 1
    if games_won_daily > games_lost_daily:
        money_daily += money_daily * 0.1
        day_won += 1
    money_total += money_daily
if day_won/days > 0.5:
    money_total += money_total * 0.2
    print(f"You won the tournament! Total raised money: {money_total:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_total:.2f}")
