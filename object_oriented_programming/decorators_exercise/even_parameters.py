def even_parameters(function):
    def wrapper(*args):
        try:
            if all(True if el % 2 == 0 else False for el in args):
                return function(*args)

        except TypeError:
            pass

        return "Please use only even numbers!"

    return wrapper


@even_parameters
def func(*args):
    return sum(args)

print(func(4, 5, 4))
