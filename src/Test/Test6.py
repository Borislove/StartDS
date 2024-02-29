# N = 25
# A = 15
# B = 10
# C = 30

A = int(input())
B = int(input())
N = int(input())
C = int(input())

L = abs(N - A)
K = abs(N - B)
M = abs(N - C)

# print(L)
# print(K)
# print(C)

"""
if N <= L and L:
    print("A")
elif N <= K and K:
    print("B")
elif N <= M and M:
    print("C")
"""

print(min(L, K, M))

