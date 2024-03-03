def star_decorator(func):          # определяем декоратор
    def wrapper(*args, **kwargs):
        print('*'*15)
        func(*args, **kwargs)
        print('*'*15)
    return wrapper

@star_decorator
def hi(name):
    return f'Привет, {name}!'

print(hi('Лена'))