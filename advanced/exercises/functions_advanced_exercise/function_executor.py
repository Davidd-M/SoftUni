def func_executor(*args):
    my_list = []
    for func, arg in args:
        my_list.append(f"{func.__name__} - {func(*arg)}")
    return '\n'.join(my_list)

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

