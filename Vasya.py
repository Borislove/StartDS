"""
Эх, Вася, Вася *
На скучном уроке математики Вася решил заняться творчеством.
Для этого в тетради в клетку он выделил прямоугольник размера N×M и стал закрашивать клетки, начиная с левого верхнего угла по спирали,
закручивающейся к центру. Примерный результат представлен на рисунке:

Для заданных значений N и M определите, сколько клеток пришлось закрасить Васе.

Входные данные
Первая строка входных данных содержит число N — высоту прямоугольника, вторая строка содержит число M — ширину прямоугольника. Оба числа - натуральные.

Выходные данные
Программа должна вывести одно целое число — количество клеток, закрашенных Васей.

Sample Input:
5
6
Sample Output:

20
"""

# side_a = int(input()) #5
# side_b = int(input()) #6
side_a = 5
side_b = 6

"""
for i in range(side_a):
    print(i, end='')
    for k in range(side_b):
        print("[ ]", end='')

    print('')
"""
a = 1
b = 0
for i in range (side_a):
    if(side_a -1 > i):
        print(a, b)



