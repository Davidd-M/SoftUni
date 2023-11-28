'''You will receive N – an integer, the number of snowballs being made by Tony and Andi.
On the following lines, you will receive 3 inputs for each snowball:
• The weight of the snowball (integer).
• The time needed for the snowball to get to its target (integer).
• The quality of the snowball (integer).'''
snowballs_num = int(input())
highest_q = 0
for snowball in range(1, snowballs_num + 1):
    weight = int(input())
    speed_time = int(input())
    quality = int(input())
    curr_q = (weight / speed_time) ** quality
    if curr_q > highest_q:
        highest_q = curr_q
        highest_we = weight
        highest_sp = speed_time
        highest_qua = quality
print(f"{highest_we} : {highest_sp} = {int(highest_q)} ({highest_qua})")