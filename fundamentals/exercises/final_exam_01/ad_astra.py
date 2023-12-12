import re

my_inp = input()
pattern = r"([#|])((?:[a-zA-Z\s]+))\1(\d{2}/\d{2}/\d{2})\1(\d{1,5})(\1|$)"
result = re.findall(pattern, my_inp)

total_cal = 0
for current_string in result:
    total_cal += int(current_string[3])
days = total_cal // 2000
print(f"You have food to last you for: {days} days!")
for current_string in result:
    item = current_string[1]
    date = current_string[2]
    calories = current_string[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
