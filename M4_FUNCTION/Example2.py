def divide(a, b):
    if b == 0:
        result = None
    else:
        result = a / b
    return result

res = divide(5,0)
print(res)
"""
if res is None:
    print('Деление на ноль невозможно.')
else:
    print(res)
"""
