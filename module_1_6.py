# создаем словарь
my_dict = {'jamaha_guitar': 65400, 'fender_guitar': 48750,'cort_guitar': 23500, 'jamaha_piano': 70100 }
print ('Прайс:', my_dict) # Выводим весь словарь
print('Существующий ключ cort_guitar:', my_dict.get('cort_guitar'))
print('НЕсуществующий ключ jamaha_fluite:', my_dict.get('jamaha_fluite'))
my_dict['jamaha_fluite'] = 4700
my_dict['bekker_piano'] = 3570879
a_deleted = my_dict.pop('jamaha_guitar') # присвоили переменной значение удаляемого элемента
print('Удаляем элемент:', a_deleted )
print (' Новый прайс:', my_dict)
# Создаем множество
my_set = { 12, 145.4, 12, 'text_1', 34, 'a', 'a', (56, 78, 89.9)}
print('Изначальное множество:', my_set)
my_set.add(12) # добавляем в множество элемент 12
my_set.add('b') # добавляем в множество элемент b
my_set.remove(34) # убираем из множества элемент 34
print('Новое множество:', my_set)