num = input()
num_str = sorted(num, reverse=True)

for i,_ in enumerate(num_str):
    print(_, end='')