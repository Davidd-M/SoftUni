"""
You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct
digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.
"""
year = int(input()) + 1

while len(set(str(year))) != len(str(year)):
    year += 1

print(year)