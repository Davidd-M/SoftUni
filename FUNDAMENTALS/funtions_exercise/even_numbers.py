nums_list = input().split()

def is_even(num):
    return int(num) % 2 == 0

even_nums = list(filter(is_even, nums_list))
even_nums = (str(even_nums)).replace("'", "")
print(even_nums)