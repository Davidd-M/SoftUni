rent = float(input())

cake = 0.2 * rent
drinks = cake * 0.55 #cake - (cake * 0.45)
animator = rent / 3

budget = rent + cake + drinks + animator

print(f'{budget:.1f}')
