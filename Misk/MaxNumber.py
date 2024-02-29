"""
Наибольшее число

Напишите программу, которая считывает одно натуральное число и выводит наибольшую цифру числа.

Входные данные
На вход подается натуральное число N (
�
⩽
1000 N⩽1000).
"""

# print(max(input()))

num = int(input())
tmp = 0
while num != 0:
    last_digit = num % 10
    num //= 10
    if (last_digit > tmp):
        tmp = last_digit
print(tmp)
