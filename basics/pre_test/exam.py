num_students = int(input())
grade_5_or_more = 0
grade_4_to_4_99 = 0
grade_3_to_3_99 = 0
grade_under_3 = 0
average = 0

for student in range(num_students):
    grade = float(input())
    if grade >= 5.00:
        grade_5_or_more += 1
        average += grade
    elif 3.99 < grade < 5.00:
        grade_4_to_4_99 += 1
        average += grade
    elif 2.99 < grade < 4.00:
        grade_3_to_3_99 += 1
        average += grade
    elif 2.99 >= grade:
        grade_under_3 += 1
        average += grade

average_grade = average / num_students
top_students = (grade_5_or_more / num_students) * 100
grade_4_to_4_99_percent = (grade_4_to_4_99 / num_students) * 100
grade_3_to_3_99_percent = (grade_3_to_3_99 / num_students) * 100
grade_under_3_percent = (grade_under_3 / num_students) * 100

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {grade_4_to_4_99_percent:.2f}%")
print(f"Between 3.00 and 3.99: {grade_3_to_3_99_percent:.2f}%")
print(f"Fail: {grade_under_3_percent:.2f}%")
print(f'Average: {average_grade:.2f}')
