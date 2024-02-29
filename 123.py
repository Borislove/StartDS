#print("Введите целое число для завершения введите 0:")

flag = True
tmp = 0
while flag:
    print("Введи число, буду складывать: Для подсчета введи 0 ")
    num = int(input())
    tmp += num
    if (num == 0):
        flag = False
        print(tmp)

"""
total = 0
while n := int(input()):
    total += n

print(total)
"""






















