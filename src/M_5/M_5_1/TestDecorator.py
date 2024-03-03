import time
from functools import wraps
import requests

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} потребовалось {end - start:.6f} секунд')
        return result
    return wrapper

@timeit
def get_webpage():

    webpage = requests.get('https://stepik.org')

get_webpage()