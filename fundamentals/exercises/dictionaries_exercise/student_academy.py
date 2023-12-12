n = int(input())
grades_dict = {}

for pair_of_rows in range(n):
    name = input()
    grade = float(input())
    if name not in grades_dict.keys():
        grades_dict[name] = []
    grades_dict[name].append(grade)

for name, grades in grades_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")
