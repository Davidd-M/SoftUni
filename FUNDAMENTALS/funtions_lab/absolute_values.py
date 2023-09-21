'''Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value
as a list. Use abs().'''

absnums_list = []
num = input().split()

for numb in num:
    numb = abs(float(numb))
    absnums_list.append(numb)

print(absnums_list)
