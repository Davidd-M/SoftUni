def exercise_func(schedule_list, lesson):
    if lesson in schedule_list and lesson + "-Exercise" not in schedule:
        lesson_index = schedule_list.index(lesson)
        schedule_list.insert(lesson_index + 1, lesson + "-Exercise")
    elif lesson in schedule_list and lesson + "-Exercise" in schedule:
        pass
    else:
        schedule_list.append(lesson)
        schedule_list.append(lesson + "-Exercise")
    return schedule_list


def insert_func(schedule_list, lesson, index):
    if lesson not in schedule_list:
        schedule_list.insert(index, lesson)
    return schedule_list


schedule = input().split(", ")

while True:
    command = input().split(":")
    if command[0] == "course start":
        for i, title in enumerate(schedule):
            print(f"{i + 1}.{title}")
        break
    elif command[0] == 'Add':
        if command[1] not in schedule:
            schedule.append(command[1])
    elif command[0] == 'Insert':
        schedule = insert_func(schedule, command[1], int(command[2]))
    elif command[0] == 'Remove':
        if command[1] in schedule:
            schedule.remove(command[1])
            if command[1] + "-Exercise" in schedule:
                schedule.remove(command[1] + "-Exercise")
    elif command[0] == 'Swap':
        lesson1 = command[1]
        lesson2 = command[2]
        if lesson1 in schedule and lesson2 in schedule:
            lesson1_index = schedule.index(lesson1)
            lesson2_index = schedule.index(lesson2)
            # Check for associated exercises
            exercise1_index = schedule.index(lesson1 + "-Exercise") if lesson1 + "-Exercise" in schedule else None
            exercise2_index = schedule.index(lesson2 + "-Exercise") if lesson2 + "-Exercise" in schedule else None
            # Swap lessons
            schedule[lesson1_index], schedule[lesson2_index] = schedule[lesson2_index], schedule[lesson1_index]
            # Swap exercises if both are found
            if exercise1_index is not None and exercise2_index is not None:
                schedule[exercise1_index], schedule[exercise2_index] = schedule[exercise2_index], schedule[
                    exercise1_index]
            # If only one exercise is found, swap it with the other lesson
            elif exercise1_index is not None:
                schedule.remove(lesson1 + "-Exercise")
                schedule.insert(lesson2_index + 1, lesson1 + "-Exercise")
            elif exercise2_index is not None:
                schedule.remove(lesson2 + "-Exercise")
                schedule.insert(lesson1_index + 1, lesson2 + "-Exercise")
    elif command[0] == 'Exercise':
        schedule = exercise_func(schedule, command[1])

