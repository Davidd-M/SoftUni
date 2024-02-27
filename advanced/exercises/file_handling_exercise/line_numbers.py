symbols = ["-", ",", ".", "!", "?", "'"]

output_file = open("output.txt", "w")

with open("text.txt", "r") as text:
    lines = text.readlines()
    index = 0
    for line in lines:
        index += 1
        line = line.rstrip()
        line_symbols = 0
        for symbol in symbols:
            if symbol in line:
                line_symbols += line.count(symbol)
        output_file.write(f"Line {index}: {line} ({len([x for x in line if x.isalpha()])})({line_symbols})\n")

output_file.close()
