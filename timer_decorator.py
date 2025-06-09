"""A decorator is simply:

. A function that takes a function as input

. And returns a new function (usually a wrapper around the original)"""

from time import sleep, time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        finish = time()

        print(f"{func.__name__} ran in {(finish-start):.2f} sec")
        return result

    return wrapper


@timer
def example_function(n):
    sleep(n)


example_function(2)