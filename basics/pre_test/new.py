n = int(input())

found = False

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                if a + b + c + d == a * b * c * d and n % 5 == 0:
                    print(f'{a}{b}{c}{d}')
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("Nothing found")
