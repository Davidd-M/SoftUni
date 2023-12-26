def age_assignment(*args, **kwargs):
    my_dict = {}
    for key in kwargs.keys():
        for name in args:
            if name[0] == key:
                my_dict[name] = int(kwargs[key])
                break
    my_dict = dict(sorted(my_dict.items(), key=lambda x: x[0]))
    return '\n'.join(f"{name} is {age} years old." for name, age in my_dict.items())


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))