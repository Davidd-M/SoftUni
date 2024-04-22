from time import time


def exec_time(func):

    def wrapper(start, end):
        start_time = time()

        func(start, end)

        return time() - start_time

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
