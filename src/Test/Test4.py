num = int(input())
sum = num
while num != 0:
    num = int(input())
    sum += num
    if num == 0:
        print(sum)