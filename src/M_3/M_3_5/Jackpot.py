"""
Джекпот
Авантюрный Петя решил сорвать джекпот в лотерее.
Для этого он стал выписывать комбинации чисел, которые выпадали в Спортлото.
Проанализировав три лотереи, он решил испытать удачу. Помогите Пете выбрать "удачные" числа.
Под удачными числами мы понимаем числа, которые выпадали в каждом розыгрыше.

Входные данные:
На вход подаются три строчки. В каждой список чисел, разделенных пробелами.

Выходные данные:

Вывести через пробел все числа выпавшие в каждом розыгрыше лотереи в порядке возрастания.
Если таких чисел не было вывести сообщение - "Удачных чисел нет".

Sample Input:

10 20 30 40 50
10 25 30 45 55
5 10 25 27 30
Sample Output:

10 30
"""

# data = list(num)  # список билетов

"""
data = list()
cnt_num = int(input())
# сделали 3 списка
for i in range(cnt_num):
    num = input().split()  # билетик
    # data = list(num)
    data.append(num)
print(data)

result = list(set(data) & set(data))
print(result)

"""

# lst_1 = [10, 22, 30, 40, 50]
# lst_2 = [10, 25, 30, 45, 55]
# lst_3 = [5, 22, 25, 30, 32]

# содержится ли 0 элемент
# print(lst_1[0] in lst_2)  # true

# num = int(input())  # 3 строчки

txt_1 = input().split(' ')
lst_1 = list(txt_1)
flag_1 = True
if (len(lst_1)) == 0:
    flag_1 = False

txt_2 = input().split(' ')
lst_2 = list(txt_2)
flag_2 = True
if (len(lst_2)) == 0:
    flag_2 = False
# lst_2.append(txt_2)

txt_3 = input().split(' ')
lst_3 = list(txt_3)
flag_3 = True
if (len(lst_3)) == 0:
    flag_3 = False
# lst_3.append(txt_3)

lst_test = []
"""
for i in range(len(lst_1)):
    if lst_2[i] in lst_1:
        lst_test.append(lst_2[i])
for i in range(len(lst_3)):
    if lst_3[i] in lst_test:
        lst_test.append(lst_3[i])
for i in range(len(lst_3)):
    if lst_3[i] in lst_test:
        lst_test.append(lst_3[i])
"""

if flag_1:
    for i in range(len(lst_1)):
        if lst_2[i] in lst_1:
            lst_test.append(lst_2[i])
    for i in range(len(lst_1)):
        if lst_3[i] in lst_test:
            lst_test.append(lst_3[i])

if flag_2:
    for i in range(len(lst_2)):
        if lst_1[i] in lst_test:
            lst_test.append(lst_1[i])
    for i in range(len(lst_2)):
        if lst_3[i] in lst_test:
            lst_test.append(lst_3[i])

if flag_3:
    for i in range(len(lst_3)):
        if lst_1[i] in lst_test:
            lst_test.append(lst_1[i])
    for i in range(len(lst_3)):
        if lst_2[i] in lst_test:
            lst_test.append(lst_2[i])

# print(lst_test)
if len(lst_test) != 0:
    # test = set(lst_test)
    # print(test)
    test = set(map(int, lst_test))
    element_1 = list(test)[0]
    element_2 = list(test)[1]
    print(int(min(lst_test)), int(max(lst_test)))
else:
    print('Удачных чисел нет')
