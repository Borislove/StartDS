# оператор not in (не находится ли значение в списке)
winter = ['Декабрь', 'Январь', 'Февраль']
month = 'Март'

if month not in winter:
    print(f'{month} - не зимний месяц.')
else:
    print(f'{month} - зимний месяц.')
