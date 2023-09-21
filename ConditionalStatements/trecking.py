groups = int(input())

musala = 0
monblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0

for i in range(0,groups):
    participants = int(input())
    total_climbers += participants
    if participants <= 5:
        musala += participants
    elif 12 >= participants >= 6:
        monblanc += participants
    elif 13 <= participants <= 25:
        kilimanjaro += participants
    elif 26 <= participants <= 40:
        k2 += participants
    else:
        everest += participants

print(f"{(musala / total_climbers) * 100:.2f}%")
print(f"{(monblanc / total_climbers) * 100:.2f}%")
print(f"{(kilimanjaro / total_climbers) * 100:.2f}%")
print(f"{(k2 / total_climbers) * 100:.2f}%")
print(f"{(everest / total_climbers) * 100:.2f}%")

