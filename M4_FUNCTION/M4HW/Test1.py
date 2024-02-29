"""
Кубик Рубика
Вова, брат Пети, очень ловко собирает кубик Рубика и уже чемпион своей школы. Пете очень бы хотелось научиться,
но не никак не выходит. Петя решил подойти основательно и разобрал кубик на части.  К своему удивлению,
 он обнаружил, что появились детали, у которых окрашено разное количество граней.
 Например, из стандартного кубика 3*3*3 получились 8 частей, у которых окрашено три грани, 12 -  две грани и 6 с одной окрашенной гранью.

Составьте программу, которая бы определяла, сколько получается окрашенных деталей из кубика Рубика размером N*N*N.



Входные данные:

Целое число N (от 1 до 100)

Выходные данные:
1 строка - количество деталей с одной окрашенной гранью
2 строка - количество деталей с двумя окрашенными гранями.
3 строка - количество деталей с тремя окрашенными гранями.

Sample Input:

3
"""
num = int(input())  # от 0 до 100
print()  # части
print(num * 4)
print()  # одна окрашенная грань
