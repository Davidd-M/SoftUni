import re

my_string = input()
cool_threshold = 1

cool_pattern = r"\d"
cool_digits = re.findall(cool_pattern, my_string)
for digit in cool_digits:
    cool_threshold *= int(digit)

emoji_pattern = r"(\:\:|\*\*)([A-Z][a-z]{2,})(\1)"
emoji_list = re.findall(emoji_pattern, my_string)
final_emojis = []
for index in range(len(emoji_list)):
    emoji_char_sum = 0
    current_emoji = emoji_list[index][1]
    for character in current_emoji:
        emoji_char_sum += ord(character)
    if emoji_char_sum > cool_threshold:
        final_emojis.append(''.join(emoji_list[index]))

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for emoji in final_emojis:
    print(emoji)
