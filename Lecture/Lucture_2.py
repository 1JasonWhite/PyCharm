# Заполнение списка:
# print('Введите 5 чисел:')
# list_1 = list()
# for i in range(5):
#     n = int(input())
#     list_1.append(n)
# print(list_1)
# print(f'В списке {len(list_1)} элемент(а)ов')


# Взаимодействие цикла for со списком:
# list_1 = [12, 2, 4, 5, 23, 53, 12]
# for i in list_1:
#     print(i)


# Не забываем, что у списка есть нумерация:
# list_1 = [12, 2, 4, 5, 23, 53, 12]
# for i in range(len(list_1)):
#     print(list_1[i])

# Удаление последнего элемента списка.
# list_1 = [12, 2, 4, 5, 23, 53, 12]
# print(f'Было: {list_1}')
# print(f'Удалили последюю цифру в списке: {list_1.pop()}')
# print(f'Стало: {list_1}')

# Удаление конкретного элемента из списка.
# list_1 = [12, 2, 4, 5, 23, 53, 12]
# print(list_1)
# print(list_1.pop(0))
# print(list_1)

# Добавление элемента на нужную позицию.
# list_1 = [12, 2, 4, 5, 23, 53, 12]
# print(list_1)
# print(list_1.insert(3, 26))
# print(list_1)

# Срез списка
# list_1 = [12, 2, 4, 5, 23, 53, 12]
# print(list_1[-2:])

'''Кортежи'''''

# tuple = (1, 2, 3, 4, 5, 6, 7)
# print(type(tuple))


# Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))


'''Словари'''
#
# dictionary = {}
# dictionary = {'up': '↑', 'down': '↓', 'left': '<', 'right': '>'}
# print(dictionary)
# print(dictionary['left'])
# del dictionary['left']
# print(dictionary)

'''Множества'''

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('yellow')
# print(colors)
# colors.add('black')
# print(colors)
# colors.remove('green')
# print(colors)

# Операции со множествами в Python:
a = {23,54,86,79,4,3,3,2,4}
b = {7, 6, 5, 4, 3, 2, 1}
c = a.copy()
print(f'print(a) {a}')
print(f'print(b){b}')
print(f'print(c) {c}')
u = a.union(b) # объединяет
print(u)
i = a.intersection(b) # пересечение
print(i)
dl = a.difference(b) # разница
print(dl)
dr = b.difference(a) # разница
print(dr)
q = a.union(b).difference(a.intersection(b))
print(q)
