def grocery_store(**kwargs):
    sorted_ls = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x))
    return '\n'.join(f"{k}: {v}" for k,v in sorted_ls)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
