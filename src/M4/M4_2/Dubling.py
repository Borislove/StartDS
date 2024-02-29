"""
Дублирование фрагмента
Дана строка, в которой буква h встречается как минимум два раза.
Повторите последовательность символов, заключенную между первым и последнием появлением буквы h два раза,
сами буквы h повторять не надо.
"""

# In the hole in the ground there lived a hobbit
# In the hole in the ground there lived a e hole in the ground there lived a hobbit

# txt = 'In the hole in the ground there lived a hobbit'
# if not 'f' in txt:
#    print()

# txt = input()
# ch = chr(104)

txt, ch = input(), chr(104)
if ch in txt:
    l_ind, r_ind = txt.index(ch), txt.rindex(ch)
    start_txt = txt[:r_ind]
    stop_txt = txt[l_ind + 1:]
    print(start_txt + stop_txt)
