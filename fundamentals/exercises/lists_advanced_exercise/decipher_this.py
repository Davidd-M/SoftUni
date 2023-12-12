secret_message_words = input().split()
_secret_message_words = []
for i, word in enumerate(secret_message_words):
    ascii_code = ""
    start_index = 0
    for j, char in enumerate(word):
        current_char = word[j]
        if current_char.isnumeric():
            ascii_code += current_char
            start_index = int(j) + 1
    word = chr(int(ascii_code)) + word[start_index:]
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    _secret_message_words.append(''.join(word))
print(*_secret_message_words)
