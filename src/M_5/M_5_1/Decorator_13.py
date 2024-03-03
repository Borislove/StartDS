import functools
def star_decorator(func):          # определяем декоратор
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '*'*15 + '\n' + result + '\n' + '*'*15
    return wrapper

@star_decorator
def hi(name):
    """Вернуть дружеское приветствие."""
    return f'Привет, {name}!'

print(hi.__name__)
print(hi.__doc__)