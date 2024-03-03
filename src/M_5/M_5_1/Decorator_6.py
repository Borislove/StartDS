def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'

    return wrapper


def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'

    return wrapper


@strong
@italic
def hi():
    return 'Привет!'


print(hi())
