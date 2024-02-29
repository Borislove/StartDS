"""

Счастливый билетик
Маша каждый день ездит в школу и обратно на трамвае.
У нее собралась коллекция билетиков. Маша считает билетик счастливым,
 если сумма первых трех цифр равна сумме последних трех. Помогите Маше сосчитать количество счастливых билетиков в ее коллекции.

Входные данные
В первой строке вводится число N - количество билетиков (

0⩽N⩽100). Далее идут N 6-значных чисел, по одному числу в строке.

Выходные данные
Выведите одно число - количество счастливых билетиков.

Sample Input:
3
123456
111300
345345
Sample Output:
2
"""
import math

k = int(input())  # кол-во билетов

# функция для подсчета суммы
def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

cnt = 0  # счетчик счастливых билетов
for _ in range(0, k):
    num = int(input())  # число нового билета
    # половиним число
    num_1 = num // 1000  # первая часть числа
    num_2 = num % 1000  # вторая часть числа
    #  увеличиваем счетчик при равных суммах
    if (sum_digits(num_1) == sum_digits(num_2)):
        cnt += 1
print(cnt)