# Добавление элементов в множество
list1 = list(range(0, 11, 2))
myset = set(list1)
print(myset)
list2 = list(range(1, 10, 2))
myset.update(list2)
print(myset)
