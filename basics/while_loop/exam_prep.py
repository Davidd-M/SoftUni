bad_grades_limit = int(input())
bad_grade = 0
grade_counter = 0
grade_sum = 0
current_task = ''
while True:
    task_name = input()
    if task_name == 'Enough':
        print(f"Average score: {grade_sum / grade_counter:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {current_task}")
        break
    current_task = task_name
    grade = int(input())
    grade_counter += 1
    grade_sum += grade
    if grade <= 4:
        bad_grade += 1
        if bad_grades_limit <= bad_grade:
            print(f"You need a break, {bad_grade} poor grades.")
            break