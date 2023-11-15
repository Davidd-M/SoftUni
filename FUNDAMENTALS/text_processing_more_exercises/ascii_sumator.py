start_symbol = input()
end_symbol = input()
string_to_iter = input()

start_ascii = ord(start_symbol)
end_ascii = ord(end_symbol)
total_sum = 0

for character in string_to_iter:
    if start_ascii < ord(character) < end_ascii:
        total_sum += ord(character)
print(total_sum)