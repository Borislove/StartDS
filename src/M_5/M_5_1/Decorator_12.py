def star_decorator(func):  # определяем декоратор
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '*' * 15 + '\n' + result + '\n' + '*' * 15

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@star_decorator
def hi(name):
    """Вернуть дружеское приветствие."""
    return f'Привет, {name}!'


print(hi.__name__)
print(hi.__doc__)
