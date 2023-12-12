import re

pattern = r"(=|/)([A-Z]{1,}[A-Za-z]{2,})\1"
my_string = input()
result = re.findall(pattern, my_string)
destination = 0
destinations = []

for current_tuple in result:
    destination += len(current_tuple[1])
    destinations.append(current_tuple[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {destination}")
