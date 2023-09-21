def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Check divisibility from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Get user input
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"True")
else:
    print(f"False")
