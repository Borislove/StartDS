"""
Крестики - нолики
Задано натуральное N. Напишите программу, которая выводит треугольник со сторонами из N нулей, заполненных "x".
На горизонтальных линиях символы разделяются одним пробелом.
Первый нолик в N-й строке должен быть первым символом в этой строке.

Sample Input:

3
Sample Output:
    0
  0 0
0 x 0
  0 0
    0
"""

num = int(input())


def print_pattern():
    S = ' '
    for i in range(num + 2):
        if i == num - 1:
            print('0')
        S += ' '
        print(S)
        if i == num - 2:
            print('')
            print('0')


print_pattern()
