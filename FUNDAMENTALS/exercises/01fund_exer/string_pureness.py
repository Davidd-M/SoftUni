'''
You will be given number n. After that, you'll receive different strings n times. Your task is to check if the given
strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore
"_":
• If a string is pure, print "{string} is pure."
• Otherwise, print "{string} is not pure!"
'''
repeats = int(input())
for string in range(repeats):
    str = input()
    pure = True
    for index, letter in enumerate(str):
        if letter == ',' or letter == '.' or letter == '_':
            print(f'{str} is not pure!')
            pure = False
            break
    if pure:
        print(f'{str} is pure.')