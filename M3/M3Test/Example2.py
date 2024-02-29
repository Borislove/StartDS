"""
Напишите программу, которая принимает список чисел в качестве входных данных и выводит сумму четных чисел в списке.

Sample Input:

8, 11, 12, 13
Sample Output:

20
"""
# numbers = [8, 11, 12, 13]
# numbers = input()
# numbers = (input())
# tmp = numbers.split()  # разбиваем. но получилось двоеточие
# print(tmp)

"""
total = 0
for i in tmp:
    if i % 2 == 0:
        total += i
print(total)
"""
"""
str = input()
lst = str.split(', ')
tmp = lst
total = 0
for i in range(len(tmp)):
    if int(tmp[i]) % 2 == 0:
        total += int(tmp[i])
print(total)
"""
#
"""
lst = input().split(', ')
total = 0
for i in range(len(lst)):
    if int(lst[i]) % 2 == 0:
        total += int(lst[i])
print(total)

"""

lst_str = input().split(', ')  # new string list
lst_int = [eval(i) for i in lst_str]  # cast to integer
total = 0
for i in range(len(lst_int)):
    if lst_int[i] % 2 == 0:
        total += lst_int[i]
print(total)
