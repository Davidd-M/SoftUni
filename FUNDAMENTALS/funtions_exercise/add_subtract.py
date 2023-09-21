int1 = int(input())
int2 = int(input())
int3 = int(input())

def add_and_subract(int1, int2, int3):
    sum_numbers = lambda int1, int2: int1 + int2
    sum = sum_numbers(int1, int2)
    subtract = lambda int1, int2: sum - int3
    subtract_result = subtract(sum, int3)
    return subtract_result
print(add_and_subract(int1, int2, int3))
