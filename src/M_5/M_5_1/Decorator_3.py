# "обернем" функцию и модифицируем её поведение
def simple_decorator(func):          # определяем декоратор
    def wrapper():
        print('Начало работы')
        func()
        print('Окончание работы')
    return wrapper

@simple_decorator
def hi():
    print('Привет!')

hi()