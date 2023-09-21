phrase = input().lower()
counter = 0
if phrase.count('sand'):
    counter += phrase.count('sand')
if phrase.count('sun'):
    counter += phrase.count('sun')
if phrase.count('fish'):
    counter += phrase.count('fish')
if phrase.count('water'):
    counter += phrase.count('water')
print(f'{counter}')