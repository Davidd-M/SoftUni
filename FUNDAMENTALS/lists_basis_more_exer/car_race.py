laps = input().split()
middle = len(laps) // 2
left = laps[:middle]
right = laps[-1:middle:-1]

def race_winner():
    left_time = 0
    right_time = 0
    winner = ''
    for lap in left:
        if float(lap) == 0:
            left_time = left_time * 0.8
        else:
            left_time += float(lap)
    for lap in right:
        if float(lap) == 0:
            right_time = right_time * 0.8
        else:
            right_time += float(lap)
    if left_time < right_time:
        winner = "left"
        return float(left_time), winner
    else:
        winner = "right"
        return float(right_time), winner


winner_time, winner = race_winner()
print(f"The winner is {winner} with total time: {winner_time:.1f}")
