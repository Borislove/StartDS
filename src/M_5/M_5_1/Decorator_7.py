def simple_decorator(func):  # определяем декоратор
    def wrapper(*args, **kwargs):
        print('Начало работы')
        print(func(*args, **kwargs))
        print('Окончание работы')

    return wrapper


@simple_decorator
def hi(name):
    return f'Привет, {name}!'


hi('Лена')
