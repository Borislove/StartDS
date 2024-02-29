n = int(input())
groom_a = abs(n - int(input()))
groom_b = abs(n - int(input()))
groom_c = abs(n - int(input()))

if min(groom_a, groom_b, groom_c) == groom_a:
    print("A")
elif min(groom_a, groom_b, groom_c) == groom_b:
    print("B")
elif min(groom_a, groom_b, groom_c) == groom_c:
    print("C")
