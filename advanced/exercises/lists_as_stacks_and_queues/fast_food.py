from collections import deque

quantity = int(input())
orders = deque(input().split())
completed_orders = 0
print(max([int(el) for el in orders]))

for order in orders:
    if int(order) <= quantity:
        quantity -= int(order)
        completed_orders += 1
    else:
        print(f"Orders left: {' '.join(list(orders)[completed_orders:])}")
        exit()

print("Orders complete")
