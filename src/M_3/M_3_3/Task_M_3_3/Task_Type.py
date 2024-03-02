"""
Метод type() *
Вам необходимо написать программу, которая принимает на вход список различных элементов и определяет,
сколько различных типов данных содержится в этом списке. Типы данных могут быть: целые числа, вещественные числа, строки и списки.

Входные данные:
На вход подается строка из элементов, разделенных запятыми.

Выходные данные:
Требуется вывести одно число - количество различных типов данных в строке.

Sample Input:
1, 2.5, "hello", [1, 2, 3], "world", 5
Sample Output:
4
"""

txt = input().replace(",", "")
tpl = tuple(txt.split())

cnt = 0
type_1 = True
type_2 = True
type_3 = True
type_4 = True
type_5 = True
type_6 = True
type_7 = True
type_8 = True
type_9 = True
test = ""

"""
for i in range(len(tpl)):
    if type_1 and int(tpl[i]):
        cnt += 1
        type_1 = False
    if type_2 and float(tpl[i]):
        cnt += 1
        type_2 = False
    if type_3 and str(tpl[i]):
        cnt += 1
        type_3 = False
    if type_4 and list(tpl[i]):
        cnt += 1
        type_4 = False
    if type_5 and (tpl[i] == True) or (tpl[i] == False):
        cnt += 1
        type_5 = False
print(cnt)
"""

for i in range(len(tpl)):
    if type_1 and int(tpl[i]):
        cnt += 1
        type_1 = False
    if type_2 and float(tpl[i]):
        cnt += 1
        type_2 = False
    if type_3 and str(tpl[i]):
        cnt += 1
        type_3 = False
    if type_4 and list(tpl[i]):
        cnt += 1
        type_4 = False
    if type_5 and (tpl[i] == True) or (tpl[i] == False):
        cnt += 1
        type_5 = False
    if type_6 and (tpl[i] is dict):
        cnt += 1
        type_6 = False
    if type_7 and (tpl[i] is set):
        cnt += 1
        type_7 = False
    if type_8 and (tpl[i] is type):
        cnt += 1
        type_8 = False
    if type_9 and (tpl[i] is None):
        cnt += 1
        type_9 = False
print(cnt)
