def sort_numbers(input_list):
    numbers = input_list
    sorted_numbers = sorted(numbers, key=int)
    sorted_numbers_int = []

    for num in sorted_numbers:
        sorted_numbers_int.append(int(num))

    return sorted_numbers_int


input_list = []
input_str = input()
try:
    while True:
        input_list.append(input_str)
        input_str = input()
except EOFError:
    pass
sorted_result = sort_numbers(input_list)
print(min(sorted_result))
