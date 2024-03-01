import time

start_time = time.time()

for i in range(100, 1000):
    sum_digit = sum(map(int, str(i)))
    if i == sum_digit * 70:
        print(i, end=' ')

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")

# 0.0010020732879638672 секунд
# 0.0010099411010742188 секунд
# 0.0009942054748535156 секунд
# 0.0010104179382324219 секунд
# 0.0010018348693847656 секунд


print('-------test---------')
start_time = time.time()

for i in range(100, 1000):
    sum_digit = sum(map(int, str(i)))
    if sum_digit * 70 == i:
        print(i, end=' ')

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")

# 0.001001596450805664 секунд
# 0.0010023117065429688 секунд
# 0.001001119613647461 секунд
