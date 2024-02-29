"""
Любимая школа
У Лены в школе занятия начинаются в 8:00. Продолжительность каждого урока — 45 минут, после 1-го, 3-го, 5-го и т.д.
уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 10 минут. Помогите Лене определить, когда заканчивается указанный урок.

Входные данные
На вход поступает номер урока (число от 1 до 10).

Выходные данные
Требуется вывести два целых числа, разделенных пробелом: время окончания урока в часах и минутах.

Sample Input:

3
Sample Output:

10 30
"""
"""
# номер урока
lesson_num = int(input())
# часы минуты
hour = 8
minute = 0
# время урока
lesson_time = 45
# перерывы
pause_5 = 5
pause_10 = 10

for _ in range(lesson_num):
    if (lesson_num % 2 == 0):
        minute += pause_10 + lesson_time
    else:
        minute += pause_5 + lesson_time
    if (minute > 60):
        hour += 1
        minute -= 60

#print('номер урока:', lesson_num)
print(hour, minute)

"""

"""
for _ in range(lesson_num):
    if (lesson_num % 2 == 0):
        minute += 10 + lesson_time
    else:
        minute += 5 + lesson_time
    if (minute >= 60):
        hour += 1
        minute -= 60
print(hour, minute)
"""
# номер урока
lesson_num = int(input())
# часы минуты
hour = 8
minute = 0
# время урока
lesson_time = 45

for _ in range(lesson_num):
    if ((lesson_num == 1) or (lesson_num == 3) or (lesson_num == 5)):
        minute += 5 + lesson_time
    if ((lesson_num == 2) or (lesson_num == 4) or (lesson_num == 6)):
        minute += 5 + lesson_time
    if (minute >= 60):
        hour += 1
        minute -= 60
print(hour, minute)

# ------------------------------------
a = int(input())
a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 10
print(a // 60 + 8, a % 60)

# ------------------------------------
n = int(input())
time = 480 + n * 45

for i in range(n - 1):
    if i % 2 == 0:
        time += 5
    if i % 2 != 0:
        time += 10

print(time // 60, time % 60)

num = int(input())
time = 480 + num * 45
for i in range(num - 1):
    if i % 2 == 0:
        time += 5
    else:
        time += 10
print(time // 60, time % 60)
