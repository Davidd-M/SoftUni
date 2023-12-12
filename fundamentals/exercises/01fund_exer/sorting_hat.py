'''
Help out the sorting hat to sort the new students in the houses of Hogwarts. You will be receiving names until the
command "Welcome!". The length of each name determines in which house the student is going:
• If the name is less than 5 chars, the student is going into Gryffindor
o Print "{name} goes to Gryffindor."
• If the name is exactly 5 chars, the student is going into Slytherin
o Print "{name} goes to Slytherin."
• If the name is exactly 6 chars, the student is going into Ravenclaw
o Print "{name} goes to Ravenclaw."
• If the name is more than 6 chars, the student is going into Hufflepuff
o Print "{name} goes to Hufflepuff."
While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end
the program. No more sorting for today!
If all students are sorted successfully, print "Welcome to Hogwarts."
'''
while True:
    name = input()
    name_len = len(name)
    if name == 'Welcome!':
        print("Welcome to Hogwarts.")
        break
    elif name == 'Voldemort':
        print("You must not speak of that name!")
        break
    elif name_len < 5:
        print(f"{name} goes to Gryffindor.")
    elif name_len == 5:
        print(f'{name} goes to Slytherin.')
    elif name_len == 6:
        print(f"{name} goes to Ravenclaw.")
    elif name_len > 6:
        print(f"{name} goes to Hufflepuff.")
