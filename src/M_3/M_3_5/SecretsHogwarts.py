"""
Тайны Хогвартса
Благодаря маховику времени Гермиона может посещать как можно большее количество уроков и познавать тайны магии.
У нее есть список самых сильных заклинаний. Чтобы держать их в тайне, она тщательно их маскирует,
записывая слова заклинания в обратном порядке. Помогите Гермионе расшифровать нужное заклинание.


Входные данные:

Программа получает на вход количество элементов N. Далее идет N строк с  зашифрованными заклинаниями.
Каждое заклинание - строка, в которой буквы всех слов записаны в обратном порядке.
Затем следует номер заклинания m, которое нужно расшифровать.

Выходные данные:

Вывести расшифрованное магическое заклинание.

Sample Input:

3
откепскЭ мунортап
муидрагниВ асоивел
аромохолА
2
Sample Output:

Вингардиум левиоса
"""
num = int(input())  # кол-во заклинаний
data = list()  # список заклинаний
for i in range(num):
    txt = input()  # новое заклинание
    lst = txt.split()
    data.append(lst)  # добавляем новое заклинание

# номер заклинания которое надо расшифровать
decoding = int(input())

if decoding != 0 and decoding < len(data):  # проверка списка
    my_string = " ".join(str(element) for element in data[1])
    words = my_string.split()
    reversed_text = " ".join(reversed(words))
    txt = reversed_text[::-1]
    print(txt.rstrip())
