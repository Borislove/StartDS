def star_decorator(func):          # определяем декоратор
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '*'*15 + '\n' + result + '\n' + '*'*15
    return wrapper

@star_decorator
def hi(name):
    return f'Привет, {name}!'

print(hi.__name__)
print(hi.__doc__)