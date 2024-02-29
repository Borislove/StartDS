# E = round
# D = print
# B = int
# A = input
E, D, B, A = round, print, int, input
C = str(A())


def F(a, b, c): A = (a + b + c) / 2;return E((A * (A - a) * (A - b) * (A - c)) ** .5, 1)


def G(a, b): return float(a * b)


def H(r): return E(r ** 2 * 3.14, 1)


if C in 'треугольник': D(F(B(A()), B(A()), B(A())))
if C in 'прямоугольник': D(G(B(A()), B(A())))
if C in 'круг': D(H(B(A())))
