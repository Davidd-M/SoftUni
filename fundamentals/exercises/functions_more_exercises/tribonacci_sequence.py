'''In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting
from 1. You will receive a positive integer number as input.
'''
def tribonacci(num:int):
    empty_list = []
    for i in range(num):
            if len(empty_list) < 1:
                empty_list = [1]
                continue
            elif len(empty_list) < 2:
                empty_list = [1, 1]
                continue
            elif len(empty_list) < 3:
                empty_list = [1, 1, 2]
                continue
            current_num = empty_list[i-1] + empty_list[i-2] + empty_list[i-3]
            empty_list.append(current_num)
    return empty_list


iterations = int(input())
print(*tribonacci(iterations))