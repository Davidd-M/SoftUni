input_list = input().split()

even_words = [x for x in input_list if len(x) % 2 == 0]
print('\n'.join(even_words))
