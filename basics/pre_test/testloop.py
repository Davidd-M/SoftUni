n = 123
a = 1
b = 9
c = 1
d = 8
print(n % 3)
if a + b + c + d == a * b * c * d and n % 5 == 0:
    print(f'{a}{b}{c}{d}')
print(a * b * c * d)
print(a + b + c + d)
print((a * b * c * d) // (a + b + c + d))
if (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
    print(f'{d}{c}{b}{a}')

x = 1