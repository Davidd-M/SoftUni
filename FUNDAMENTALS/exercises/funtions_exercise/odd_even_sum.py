num = int(input())

def sum_even_odd(ints):
    sum_even = 0
    sum_odd = 0
    ints = str(ints)
    for i, cha in enumerate(ints):
        cha = int(cha)
        if cha % 2 == 0:
            sum_even += cha
        else:
            sum_odd += cha
    return sum_even, sum_odd

sum_even, sum_odd = sum_even_odd(num)
print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
