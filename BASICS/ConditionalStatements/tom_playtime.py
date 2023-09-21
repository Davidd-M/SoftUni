rest_days = int(input())

norm = 30000

workday_playtime = 63
restday_playtime = 127

workdays_yearly = 365 - rest_days
playtime_total = (workdays_yearly * workday_playtime) + (rest_days * restday_playtime)
norm_difference = abs(norm - playtime_total)
playtime_total_hours = norm_difference // 60
playtime_total_mins = norm_difference % 60


if playtime_total > norm:
    print('Tom will run away')
    print(f'{playtime_total_hours} hours and {playtime_total_mins} minutes more for play')
elif playtime_total < norm:
    print('Tom sleeps well')
    print(f'{playtime_total_hours} hours and {playtime_total_mins} minutes less for play')


