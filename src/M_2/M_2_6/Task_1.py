"""
Наибольшее число
Напишите программу, которая считывает одно натуральное число и выводит наибольшую цифру числа.

Входные данные
На вход подается натуральное число N (N⩽1000).
"""

# print(max(input()))

num = int(input())
max_digit = 0
while num != 0:
    last_digit = num % 10
    num //= 10
    if last_digit > max_digit:
        max_digit = last_digit
print(max_digit)