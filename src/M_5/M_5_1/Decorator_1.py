
# принимает на вход другую функцию и возвращает ее
def empty_decorator(func):
    return func


def hi():
    print('Привет!')

hi = empty_decorator(hi)      # декорируем функцию

hi()


