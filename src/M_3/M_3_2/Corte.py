from sys import getsizeof

numbers1 = ((1, 2, 3), (4, 5, 6), (1, 2, 3))
numbers2 = [[1, 2, 3], [4, 5, 6], [4, 5, 6]]
print(getsizeof(numbers1))
print(getsizeof(numbers2))
