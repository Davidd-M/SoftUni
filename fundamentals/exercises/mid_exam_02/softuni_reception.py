employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students = int(input())

employees_efficiency = employee1_efficiency + employee2_efficiency + employee3_efficiency
hour = 0

if students == 0:
    print(f"Time needed: {hour}h.")
    exit()

while True:
    hour += 1
    if hour % 4 == 0:
        hour += 1
    students -= employees_efficiency
    if students <= 0:
        print(f"Time needed: {hour}h.")
        break
