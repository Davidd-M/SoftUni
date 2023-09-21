key = int(input())
lines = int(input())
word = []
for _ in range(lines):
    letter = ord(input()) + key
    word.append(chr(letter))
word = ''.join(word)
print(f'{word}')