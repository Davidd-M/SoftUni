from collections import deque

pocket_money = [int(x) for x in input().split()]
prices = deque(map(int, input().split()))
foods = 0

while pocket_money and prices:
    current_money = pocket_money.pop()
    current_price = prices.popleft()
    if current_money == current_price:
        foods += 1
    elif current_money > current_price:
        foods += 1
        if pocket_money:
            pocket_money[-1] += current_money - current_price

if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.")
elif foods:
    if foods == 1:
        print(f"Henry ate: {foods} food.")
    else:
        print(f"Henry ate: {foods} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")