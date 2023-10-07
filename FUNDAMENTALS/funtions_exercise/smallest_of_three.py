def sort_numbers(input_string):
    numbers = input_string.split()
    sorted_numbers = sorted(numbers, key=int)
    sorted_numbers_int = []

    for num in sorted_numbers:
        sorted_numbers_int.append(int(num))

    return sorted_numbers_int


input_string = input()
sorted_result = sort_numbers(input_string)
print(sorted_result)
