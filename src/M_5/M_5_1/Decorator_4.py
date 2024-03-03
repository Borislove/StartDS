def simple_decorator(func):          # определяем декоратор
    def wrapper():
        print('Начало работы')
        func()
        print('Окончание работы')
    return wrapper

def hi():
    return 'Привет!'

print(hi)
hi = simple_decorator(hi)     # ручное декорирование
print(hi)