"""
Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
1 British Pound = 1.31 Dollars
"""
pound = int(input())
usd = pound * 1.31
print(f'{usd:.3f}')