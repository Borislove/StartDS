# декоратор в удобном виде
def empty_decorator(func):
    return func


@empty_decorator  # декорируем функцию
def hi():
    print('Привет!')


hi()
