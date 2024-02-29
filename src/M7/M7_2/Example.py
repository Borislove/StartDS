import numpy as np
import statistics

"""
Чему равна несмещенная выборочная дисперсия набора данных? Ответ округлите до целого числа.

"""
numbers = np.loadtxt("numbers.csv", delimiter=",")
print('Несмещенная выборочная дисперсия', statistics.variance(numbers))
print('Несмещенная выборочная дисперсия округленная', round(statistics.variance(numbers)))

# тоже прокатит
# print(np.var(numbers, ddof=1))
