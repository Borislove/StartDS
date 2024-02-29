import numpy as np
import statistics

numbers = np.loadtxt("numbers.csv", delimiter=",")
print(numbers)

# ищем среднее
# mean = np.mean(numbers)
# округляем до целого числа
# print(mean)
# print(round(mean))

# median = np.median(numbers)
# print(median)
# print(round(median))

print(statistics.mode(numbers))
print(statistics.multimode(numbers))

"""
price_counts = {}
for p in numbers:
    if p not in price_counts:
        numbers[p] = 1
    else:
        numbers[p] += 1

maxp = 0
mode_price = None
for k, v in price_counts.items():
    if maxp < v:
        maxp = v
        mode_price = k
print(mode_price, maxp)
"""
print(numbers)
#print("Mode of given data set is % s" % (statistics.mode(numbers)))