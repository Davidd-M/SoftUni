import re

n = int(input())

pattern = r"(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1"


for _ in range(n):
    password = input()
    result = re.findall(pattern, password)
    if result:
        print(f"Password: {''.join(result[0][1:])}")
    else:
        print("Try another password!")