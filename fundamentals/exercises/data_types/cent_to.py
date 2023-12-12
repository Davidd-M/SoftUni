"""
Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
Examples
Input Output
1 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes
5 5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes
Hints
• Assume that one year has 365.2422 days on average (the Tropical year).
"""
ceentureis = int(input())
ceentureis_years = ceentureis * 100
centureies_days = int(ceentureis_years * 365.2422)
centureies_hours = centureies_days * 24
centureies_mins = centureies_hours * 60
print(f'{ceentureis} centuries = {ceentureis_years} years = {centureies_days} days = {centureies_hours} hours = {centureies_mins} minutes')