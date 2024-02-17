size = int(input())
my_pos = ()
armor_value = 300
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
airspace = []
enemies = 0

for row in range(size):
    current_row = list(input())
    if "J" in current_row:
        my_pos = (row, int(current_row.index("J")))
    if "E" in current_row:
        enemies += current_row.count("E")
    airspace.append(current_row)

while armor_value > 0:
    command = input()
    airspace[my_pos[0]][my_pos[1]] = "-"
    r, c = directions[command][0] + my_pos[0], directions[command][1] + my_pos[1]
    my_pos = (r, c)
    if airspace[r][c] == "E":
        airspace[r][c] = "-"
        enemies -= 1
        if enemies == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            # TODO FINAL
            break
        armor_value -= 100
        if armor_value < 1:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")
            # TODO FINAL
            break
    elif airspace[r][c] == "R":
        airspace[r][c] = "-"
        armor_value = 300
    else:
        airspace[r][c] = "-"

airspace[r][c] = "J"
[print(*row, sep="") for row in airspace]