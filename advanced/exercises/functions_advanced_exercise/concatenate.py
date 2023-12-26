def concatenate(*args, **kwargs):
    args_str = ''.join(args)
    for word in kwargs.keys():
        if word in args_str:
            args_str = args_str.replace(word, kwargs[word])
    return args_str


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))