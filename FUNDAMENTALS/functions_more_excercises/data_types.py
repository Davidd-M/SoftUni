def data_type(some_type: str, value):
    if some_type == 'int':
        return int(value) * 2
    elif some_type == "real":
        return f"{float(value) * 1.5:.2f}"
    else:
        return f"${value}$"


type_of_data = input()
value_of_data = input()
print(data_type(type_of_data, value_of_data))

