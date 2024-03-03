import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        arg_str = ', '.join(repr(arg) for arg in args)
        if arg_str != '':
            print(f'{func.__name__}({arg_str}) потребовалось {end - start:.6f} секунд')
        else:
            print(f'{func.__name__} потребовалось {end - start:.6f} секунд')
        return result

    return wrapper


@timeit
def countdown(n, step):
    while n > 0:
        n -= step


countdown(10 ** 5, 2)
countdown(10 ** 8, 5)
