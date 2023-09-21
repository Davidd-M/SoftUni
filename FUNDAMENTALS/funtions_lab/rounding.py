'''
Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use
round().
'''
nums_input_list = input().split()


def rounder(nums_list):
    rounded_list = []
    for num in nums_list:
        rounded_list.append(round(float(num)))
    return rounded_list

print(rounder(nums_input_list))