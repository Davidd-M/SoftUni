def division(num1, num2):

    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Division by zero!")
        main()


def multiplication(num1, num2):
    result = num1 * num2
    return result


def subtraction(num1, num2):
    result = num1 - num2
    return result


def addition(num1, num2):
    result = num1 + num2
    return result


def main():
    operation = ''
    number1 = 0
    number2 = 0
    result = ''
    print("Menu\n"
          "\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division \n"
          "5. Quit")
    while True:
        try:
            operation = float(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid operation!")
            continue
        if 0 > operation or operation > 5:
            print("Operation should be between 1 and 5!")
            continue
        if operation == 1:  # Addition
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = addition(number1, number2)
        if operation == 2:  # Subtraction
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = subtraction(number1, number2)
        if operation == 3:  # Multiplication
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = multiplication(number1, number2)
        if operation == 4:  # Division
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            result = division(number1, number2)
        if operation == 5:  # Quit
            print("Quit!")
            quit()
        # Print the result
        if result.is_integer():
            print(f"Result = {int(result)}")
        else:
            print(f"Result = {result}")


if __name__ == '__main__':
    main()
