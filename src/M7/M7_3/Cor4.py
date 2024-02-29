import numpy as np

x, y = [-1, 0, 5, -3, 6, 7, 0], [5, 7, 3, 8, 4, 6, 5]
corr = np.corrcoef(x, y)
print(corr)

num = -0.59450499
print(round(num, 2))

"""
X = [-1, 0, 5, -3, 6, 7, 0]
Y = [5, 7, 3, 8, 4, 6, 5]

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

dif_x = [x - mean_x for x in X]
dif_y = [y - mean_y for y in Y]

numerator = sum([dif_x[elem] * dif_y[elem] for elem in range(len(dif_x))])
denominator = (sum([x ** 2 for x in dif_x]) * sum([y ** 2 for y in dif_y])) ** 0.5

r = numerator / denominator
print(round(r, 2))
"""
