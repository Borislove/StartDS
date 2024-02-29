"""
Первое и последнее вхождение
Дана строка. Если в этом числе буква f встречается только один раз,
выведите её индекс. Если она встречается два и более раз,
выведите индекс её первого и последнего появления.
Если буква f в данной строке не встречается, ничего не выводите. При решении этой задачи нельзя использовать метод count и циклы.
"""

# comfort   3
# comfortf   3
# подстрока не найдена...хаха
txt = input()
if not 'f' in txt:
    print()

if 'f' in txt:
    l_ind = txt.index('f')
    r_ind = txt.rindex('f')
    tmp = l_ind - r_ind
    if tmp == 0:
        print(l_ind)
    else:
        print(l_ind, r_ind)
        # print(r_ind)

"""
D='f'
C=print
A=input()
B=A.index(D)
E=A.rindex(D)
F=0
if D in A:
	F=B-E
	if F==0:C(B)
	else:C(B);C(E)
"""

C, A, B = print, 'f', input()
if not A in B: C()
if A in B:
    D = B.index(A);
    E = B.rindex(A);
    F = D - E
    if F == 0:
        C(D)
    else:
        C(D, E)
