'''You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative,
positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.
'''
def multiplic_sign(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    negatives = [num1, num2, num3]
    negative_nums = 0
    for i in negatives:
        if i < 0:
            negative_nums += 1
    if negative_nums == 2 or negative_nums == 0:
        return "positive"
    else:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = multiplic_sign(num1, num2, num3)
print(result)
