# m , a
a = list(str.lower(input()))
k = list(set(a))
c = 0 # переменные
d = 0
b = set("aeiouаеёиоуыэюя")  # список, глассные

for i in k:
    if i in b:
        print(i)
        c += 1
    else:
        print(i)
        d += 1

p = (c,d)
print(p)

# привет как дела1
