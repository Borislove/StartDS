ch = chr(102)


def test(txt, s):
    find = txt.find(s)
    if find != -1:
        test = txt.find(s, find + 1)
        return test if test != -1 else -1
    else:
        return -2

print(test(input(), ch))

