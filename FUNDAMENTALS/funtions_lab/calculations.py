operator = input()
num_1 = int(input())
num_2 = int(input())


def calculator(operator, num_1, num_2):
    result = None
    if operator == 'multiply':
        result = num_1 ** num_2
    elif operator == "divide":
        result = num_1 // num_2
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result
print(calculator(operator, num_1, num_2))