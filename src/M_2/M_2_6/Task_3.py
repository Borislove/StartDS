"""
Следующее четное
Напишите программу, которая считывает одно целое число и выводит следующее за ним четное число.

Входные данные
На вход подается число N.

Выходные данные
Программа выводит следующее за N четное число.
"""

"""
num = int(input())
if num % 2 == 0:
    num += 2
    print(num)
else:
    num += 1
    print(num)
"""

"""
num = int(input())
if num % 2 == 0:
    print(num + 2)
else:
    print(num + 1)
"""

num = int(input())
print(num + 2) if num % 2 == 0 else print(num + 1)
