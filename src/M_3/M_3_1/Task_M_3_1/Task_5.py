"""
Сумма четных чисел
Напишите программу, которая принимает список чисел в качестве входных данных и выводит сумму четных чисел в списке.

Sample Input:
8, 11, 12, 13
Sample Output:
20
"""
lst_str = input().split(', ')  # new string list
lst_int = [eval(i) for i in lst_str]  # cast to integer
total = 0
for i in range(len(lst_int)):
    if lst_int[i] % 2 == 0:
        total += lst_int[i]
print(total)
