"""
15 1 -> False
2 -> False
3 -> False
4 -> False
5 -> True
6 -> False
7 -> True
8 -> False
9 -> False
10 -> False
11 -> False
12 -> False
13 -> False
14 -> True
15 -> False
6 1 -> False
2 -> False
3 -> False
4 -> False
5 -> True
6 -> False
Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number and if it is special
or not (True / False). A number is special when the sum of its digits is 5, 7, or 11.
Examples
Input Output
"""
n_num = int(input())
sum = 0
for number in range(1,n_num + 1):
    sum = 0
    n_num_list = str(number)
    for i, char in enumerate(n_num_list):
        sum += int(char)
    if sum == 5 or sum == 7 or sum == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')