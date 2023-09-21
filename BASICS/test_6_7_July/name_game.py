points = 0
max_points = 0
winner = ''

while True:
    player = input()
    if player == 'Stop':
        break
    name_len = len(player)
    points = 0
    for i in range(name_len):
        num = int(input())
        if num == ord(player[i]):
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner = player

print(f"The winner is {winner} with {max_points} points!")
