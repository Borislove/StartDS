# v2

def sum_digits(n):
    return sum(map(int, str(n)))


cnt = 0
for _ in range(0, int(input())):
    num = int(input())
    if sum_digits(num // 1000) == sum_digits(num % 1000):
        cnt += 1
print(cnt)
