
fig = str(input())


if fig in 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2  # периметр
    s = p * (p - a) * (p - b) * (p - c)  # площадь
    s = s ** 0.5
    print(round(s, 1))
if fig in 'прямоугольник':
    a, b = int(input()), int(input())
    print(float(a * b))
if fig in 'круг':
    r = int(input())
    s = r ** 2 * 3.14
    print(round(s, 1))
