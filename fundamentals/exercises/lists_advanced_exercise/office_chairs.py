number_of_rooms = int(input())
difference = 0

for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    difference += chairs - visitors
    if visitors > chairs:
        print(f"{abs(chairs - visitors)} more chairs needed in room {room}")
if difference >= 0:
    print(f"Game On, {difference} free chairs left")
