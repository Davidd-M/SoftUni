symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as text:
    lines = text.readlines()[::2]
    for line in lines:
        for symbol in symbols:
            line = line.replace(symbol, "@")
        print(*line.split()[::-1])
