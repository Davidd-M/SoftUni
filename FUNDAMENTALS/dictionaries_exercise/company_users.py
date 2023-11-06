companies_dict = dict()

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if company_name not in companies_dict:
        companies_dict[company_name] = []
    if employee_id not in companies_dict[company_name]:
        companies_dict[company_name].append(employee_id)

for k, v in companies_dict.items():
    print(f"{k}")
    for ID in v:
        print(f"-- {ID}")