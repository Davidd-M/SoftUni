for _ in range(int(input())):
    line = input()
    if ("@" and "|" and "#" and "*") in line:
        name_start = line.find("@") + 1
        name_end = line.find("|")
        age_start = line.find("#") + 1
        age_end = line.find("*")
        print(f"{line[name_start:name_end]} is {line[age_start:age_end]} years old.")

