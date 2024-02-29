"""
Удаление фрагмента
Дана строка, в которой буква h встречается минимум два раза.
Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
"""
# test input
# In the hole in the ground there lived a hobbit
# txt = input()
txt = 'In the hole in the ground there lived a hobbit'
l_ind = txt.index('h')
r_ind = txt.rindex('h')
left = txt[:l_ind]
right = txt[r_ind + 1:]
print(left + right)
