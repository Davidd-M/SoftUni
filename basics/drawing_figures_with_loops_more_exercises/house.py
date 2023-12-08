n = int(input())

for i in range(1, (n + 1) // 2):
    if n % 2 != 0:
        print("-" * ((n // 2) - (i - 1)) + "*" * i + "*" * (i - 1) + "-" * ((n // 2) - (i - 1)))
    else:
        print("-" * ((n // 2) - i) + "*" * i + "*" * i + "-" * ((n // 2) - i))
print("*" * n)
for i in range((n // 2)):
    print("|" + "*" * (n - 2) + "|")