input_str = input()
mask = ['a', 'o', 'u', 'e', 'i']
new_str = ''.join([x for x in input_str if x.lower() not in mask])
print(new_str)