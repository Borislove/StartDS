def swapcase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.swapcase()
        return modified_result

    return wrapper


@swapcase
def hi():
    return 'Привет!'


