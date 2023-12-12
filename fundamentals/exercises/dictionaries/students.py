people_dict = {}
course_to_print = None

while True:
    command = input()
    if ":" not in command:
        course_to_print = command[:4]
        break
    name, ID, course = command.split(":")
    people_dict[ID] = [name, course]

for ID, value in people_dict.items():
    name, course = value[0], value[1]
    if course_to_print in course:
        print(f"{name} - {ID}")
