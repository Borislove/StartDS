word = input().lower()
f = 'f'
index = word.find(f)
rindex = word.rfind(f)
if index == rindex and index > -1:
    print(-1)
elif index == -1:
    print(-2)

print(index > -1)
