'''Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min
and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
The output should be as follows:
• On the first line: "The minimum number is {minimum number}"
• On the second line: "The maximum number is {maximum number}"
• On the third line: "The sum number is: {sum of all numbers}"'''

sequence = input()

def min_max(sequence):
    numbers = [int(num) for num in sequence.split()]
    min_num = min(numbers)
    max_num = max(numbers)
    sum_num = sum(numbers)
    return min_num, max_num, sum_num

min_num, max_num, sum_num = min_max(sequence)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")



