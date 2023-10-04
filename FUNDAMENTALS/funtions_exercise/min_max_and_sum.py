"""Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min 
and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
The output should be as follows:
• On the first line: "The minimum number is {minimum number}"
• On the second line: "The maximum number is {maximum number}"
• On the third line: "The sum number is: {sum of all numbers}"""

int_list = input().split()


def min_max(int_lists):
    modified_list = [int(x) for x in int_lists]
    return min(modified_list), max(modified_list), sum(modified_list)


minimum, maximum, summ = min_max(int_list)
print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}" )
print(f"The sum number is: {summ}")