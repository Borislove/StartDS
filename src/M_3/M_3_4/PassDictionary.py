# обход словаря
ita_rus = {'cielo': 'небо', 'oggi': 'сегодня', 'bellа': 'красивая', 'donna': 'женщина'}
for elem in ita_rus:
    print(elem)

# обход по значениям

ita_rus = {'cielo': 'небо', 'oggi': 'сегодня', 'bellа': 'красивая', 'donna': 'женщина'}
for elem in ita_rus.values():
    print(elem)

# перебор ключ-значение
ita_rus = {'cielo': 'небо', 'oggi': 'сегодня', 'bellа': 'красивая', 'donna': 'женщина'}
for elem in ita_rus.items():
    print(elem)

# ключ - значение - присвоение переменным
ita_rus = {'cielo': 'небо', 'oggi': 'сегодня', 'bellа': 'красивая', 'donna': 'женщина'}
for ita, rus, in ita_rus.items():
    print(f'{ita} - {rus}')
