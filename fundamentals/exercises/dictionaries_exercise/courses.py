courses_dict = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name not in courses_dict.keys():
        courses_dict[course_name] = []
    courses_dict[course_name].append(student_name)

for k, v in courses_dict.items():
    print(f"{k}: {len(v)}")
    for person in v:
        print(f"-- {person}")
