words_list = input().split(" | ")

morse_code_dict = {
    '.-': 'A',   '-.': 'N',
    '-...': 'B', '---': 'O',
    '-.-.': 'C', '.--.': 'P',
    '-..': 'D',  '--.-': 'Q',
    '.': 'E',    '.-.': 'R',
    '..-.': 'F', '...': 'S',
    '--.': 'G',  '-': 'T',
    '....': 'H', '..-': 'U',
    '..': 'I',   '...-': 'V',
    '.---': 'J', '.--': 'W',
    '-.-': 'K',  '-..-': 'X',
    '.-..': 'L', '-.--': 'Y',
    '--': 'M',   '--..': 'Z'
}
result = []
for word in words_list:
    letters = word.split()
    current_word = ""
    for letter_code in letters:
        current_word += morse_code_dict[letter_code]
    result.append(current_word)
print(*result)