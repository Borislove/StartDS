"""
 Подсчет количества гласных и согласных
Напишите программу, которая принимает на вход слово от пользователя и подсчитывает количество гласных
 и согласных в этом слове. Результат подсчета необходимо представьте в виде кортежа:
(количество гласных, количество согласных)

Примечание:

Регистр букв (верхний или нижний) не должен учитываться при подсчете (вам поможет метод str.lower())
Одинаковые буквы в слове учитываются лишь 1 раз
Sample Input:

мама
Sample Output:

(1, 1)
"""
# vowel_letter = ("а, у, о, ы, и, э, я, ю, ё, е")
# consonant_letters = ("б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ")
# txt = 'мама'
"""

txt = input().lower()
lst = list(set(txt))

vowel_letter = ("aeiouаеёиоуыэюя")
consonant_letters = ("bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ")

cnt_1 = 0
cnt_2 = 0
for i in lst:
    if i in vowel_letter:
        cnt_1 += 1
    if i in consonant_letters:
        cnt_2 += 1

tpl = (cnt_1, cnt_2)
print(tpl)
"""

lst = set(input().lower())
tpl_1, tpl_2 = ("aeiouаеёиоуыэюя"), ("bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ")

cnt_1, cnt_2 = 0, 0
for i in lst:
    if i in tpl_1:
        cnt_1 += 1
    if i in tpl_2:
        cnt_2 += 1

print((cnt_1, cnt_2))
