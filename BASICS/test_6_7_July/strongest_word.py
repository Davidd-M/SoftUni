import math
asci = 0
max_ascii = 0
strongest_word = ''

while True:
    word = input()
    if word == 'End of words':
        break
    asci = 0
    for i in range(len(word)):
        asci += ord(word[i])
    first_letter = word[0]
    if first_letter == 'a' or first_letter == 'A':
        asci *= len(word)
    elif first_letter == 'e' or first_letter == 'E':
        asci *= len(word)
    elif first_letter == 'i' or first_letter == 'I':
        asci *= len(word)
    elif first_letter == 'o' or first_letter == 'u':
        asci *= len(word)
    elif first_letter == 'u' or first_letter == 'o':
        asci *= len(word)
    elif first_letter == 'y' or first_letter == 'Y':
        asci *= len(word)
    else:
        asci /= len(word)
        asci = math.floor(asci)
    if asci > max_ascii:
        max_ascii = asci
        strongest_word = word
print(f"The most powerful word is {strongest_word} - {max_ascii}")
