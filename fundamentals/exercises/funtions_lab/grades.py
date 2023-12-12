'''
2.00 – 2.99 - "Fail"
• 3.00 – 3.49 - "Poor"
• 3.50 – 4.49 - "Good"
• 4.50 – 5.49 - "Very Good"
• 5.50 – 6.00 - "Excellent"
'''

grade = float(input())

def with_words(grade):
    if 3.00 > grade > 1.99:
        grade = 'Fail'
    elif 2.99 < grade < 3.50:
        grade = 'Poor'
    elif 3.49 < grade < 4.50:
        grade = 'Good'
    elif 4.49 < grade < 5.50:
        grade = 'Very Good'
    elif grade > 5.49:
        grade = 'Excellent'
    return grade

print(with_words(grade))