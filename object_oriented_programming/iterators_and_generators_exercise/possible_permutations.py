from itertools import permutations

def possible_permutations(num_list):
    for el in permutations(num_list):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
