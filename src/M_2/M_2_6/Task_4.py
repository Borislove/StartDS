"""
Разборчивая невеста
У разборчивой невесты есть любимые цветы - розы и любимое их количество в букете.
Поэтому при выборе женихов она руководствуется правилом: "жених должен подарить почти идеальный букет из роз".
По известному любимому числу невесты - N и количества роз в букетах от женихов: A , B и C штук
(все дарят разные букеты, отличающиеся от идеального по-разному), определите, которого она выберет.

Входные данные
На вход программе подается четыре числа, по одному в строке:
- в первой строке - любимое число невесты;
- в следующих трёх - количество роз в букетах женихов (A, B и C соответственно).

Выходные данные
Вывести букву жениха (A, B или C), которого выберет невеста
"""

love_number = int(input())  # любимое число
num_a = int(input())
num_b = int(input())
num_c = int(input())

dst_a = abs(love_number - num_a)
dst_b = abs(love_number - num_b)
dst_c = abs(love_number - num_c)

# print(min(dst_a, dst_b, dst_c))

if dst_a < dst_b and dst_a < dst_c:
    print('A')
if dst_b < dst_a and dst_b < dst_c:
    print('B')
if dst_c < dst_a and dst_c < dst_b:
    print('C')
