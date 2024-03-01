# Треугольник ли
"""
По трем натуральным числам a, b, c определите, существует ли треугольник с такими сторонами.
Если треугольник существует, выведите строку YES, иначе выведите строку NO.
Напомним, что каждая сторона треугольника всегда меньше суммы двух других (неравенство треугольника).

Входные данные
На вход программе подается три числа a, b, c(стороны треугольника), по одному в строке.

Выходные данные
Программа выводит YES, если существует треугольник с такими сторонами, NO - в противном случае.

Sample Input:
5
3
2
Sample Output:
NO
"""

a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < b + a:
    print("YES")
else:
    print("NO")