from statistics import variance

import numpy as np

# Вычислите несмещенную выборочную дисперсию набора данных
#
# -3, 5, -2, 8, 7


lst = [-3, 5, -2, 8, 7]
# lst = [8, 6, 0, 10]
# lst = [3, 5, 10, 12]
print('original: ')
print(lst)
print('sorted: ')
print(sorted(lst))
print('Длина:', len(lst))

print('Размах:', max(lst) - min(lst))  # 11

mean = np.mean(lst)
print('Среднее значение набора:', mean)  # 3.0

# дисперсия
# print(np.var(lst))  # 21.2
disp = np.var(lst)
print('Дисперсия:', disp)

# генеальная
print('Генеральное среднее:', sum(lst) / len(lst))

# выборочная дисперсия данных
print('Несмещенная выборочная дисперсия', variance(lst))
