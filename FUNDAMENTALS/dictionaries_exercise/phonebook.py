phonebook = {}
n = 0

while True:
    contact = input()
    if "-" not in contact:
        n = int(contact)
        break
    name, number = contact.split("-")
    phonebook[name] = number

for i in range(n):
    person_to_find = input()
    if person_to_find not in phonebook.keys():
        print(f"Contact {person_to_find} does not exist.")
    else:
        print(f"{person_to_find} -> {phonebook[person_to_find]}")


