# Колекции
# списки
# множества
# кортежи
# словари

# 1 списки - изменяемый

# my_list = [1, '2', True, [4, 5], {'key': 34}]

# print(my_list[4])

# a = [1, 2, 3]
# b = a
# a.append(4) # в А добавили 4-ку и в b будет так же
# print(a)
# print(b)
# print(a) [1, 2, 3, 4]
# print(b) [1, 2, 3, 4]

# чтобы не изменялось
# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
# b.append(5)
# print(a) # [1, 2, 3, 4]
# print(b) # [1, 2, 3, 5]

# ВАЖНО !!!
# a = [1, 2, 3, [1, 2, 3]]
# b = a.copy()
# a[3][1] = 9
# print(a) # [1, 2, 3, [1, 9, 3]]
# print(b) # [1, 2, 3, [1, 9, 3]]
'''9ка и там и там, хотя  мы делали копию А
Дело в том, что a.copy копирует только ОСНОВНОЙ список
а не все вместе
'''
# import random

# ВАЖНО !!!
# from copy import deepcopy
# '''from copy import deepcopy для глубокой копии списка'''
#
# a = [1, 2, 3, [1, 2, 3]]
# b = deepcopy(a)
# a[3][1] = 9
# print(a) # [1, 2, 3, [1, 9, 3]]
# print(b) # [1, 2, 3, [1, 2, 3]]


# my_list = [1, 2, 3]
#
# my_string = '123'
#
# print(my_list[1])
# print(my_string[1])


# my_list = [1, 2, 3]

# my_string = '123'
# my_string = list(my_string)
#
# print(my_list)
# print(my_string)


# метод append
# my_list = [1, 2, 3]
# my_list.append(4) # добавляется ТОЛЬКО в конец !!!
# print(my_list) # [1, 2, 3, 4]


# метод insert - добавляется ТОЛЬКО по индексу
# my_list = []
#
# my_list.insert(0, 'A')
# print(my_list)
# my_list.insert(0, 'B')
# print(my_list)
# my_list.insert(0, 'C')
# print(my_list)
# my_list.insert(0, 'D')
# print(my_list)
# my_list.insert(0, 'E')
# print(my_list)
# ['A']
# ['B', 'A']
# ['C', 'B', 'A']
# ['D', 'C', 'B', 'A']
# ['E', 'D', 'C', 'B', 'A']
# ['E', 'D', 'C', 'B', 'A']
# print(my_list)



# метод pop - удаляет с конца списка

# my_list = [1, 2, 3, 4]
#
# my_list.pop() # либо удалить по индексу, написать в скобках индекс. По
#               # дефолту, удаляет с конца
#
# print(my_list) # [1, 2, 3]


# метод remove
# my_list = [1, 2, 3, 2, 4]
#
# my_list.remove(2) # удаляет по значению, если их несколько, то удаляет первую попавшуюся
#
# print(my_list) # [1, 3, 4]


# count
# my_list = [1, 2, 3, 4, 5]
# print(my_list.count(2))
# print(my_list)

# index - ищет под каким индексом стоит элемент
# my_list = [1, 2, 3, 4, 5]
# print(my_list.index(2))
# print(my_list)

# reverse
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list) # [5, 4, 3, 2, 1]

# СРЕЗЫ
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# print(my_list[1:3:1]) # [2, 3]
# print(my_list[1::2]) # [2, 4, 6, 8]


# my_list = ['1', '2', '3', '4', '5', '6', '7', '8']
# print('-'.join(my_list)) # 1-2-3-4-5-6-7-8


'''--------- КАРТЕЖИ ----------'''
# tuple(картеж) - неизменяемый
# tuple
#
# my_tuple = (1, 2, 3, 'r', [1, 3, 45, 6])
# my_tuple[-1][-1] = 'AAAAA'
# print(my_tuple) # (1, 2, 3, 'r', [1, 3, 45, 'AAAAA'])

# tuple
''''перевели картеж в список и тогда можем его изменять'''
# my_tuple = (1, 2, 3, 'r', [1, 3, 45, 6])
# my_tuple = list(my_tuple)
# my_tuple[3] = 'egwerywtry'
# print(my_tuple)

# tuple
# my_tuple = (1, 2, 3, 'r')
#
# dig1, dig2, dig3, let = my_tuple
# print((dig1))
# print((dig2))
# print((dig3))
# print((let))
# 1
# 2
# 3
# r


# tuple
# my_tuple = (1, 2, 3, 'r')
#
# dig1, dig2, *dig3 = my_tuple
# print((dig1))
# print((dig2))
# print((dig3))
# 1
# 2
# [3, 'r']


# tuple
#
# my_tuple = (1, 2, 3, 'r')
# print(*my_tuple) # * в print вывод БЕЗ скобок
# print(*my_tuple, sep='-') # 1-2-3-r
# print(*my_tuple, sep='\n')
'''картеж из 1го элемента не может написан my_tuple = (1) - будет int
, добавить нужно запятую my_tuple = (1,) - будет tuple(картеж)'''



'''ТИП ДАННЫХ set - множество. Неупорядоченное. Множество хранит множество НЕИЗМЕНЯЕМЫХ объектов'''


# set = {1,2,3,4,5,6,6}
# print(set) # {1, 2, 3, 4, 5, 6}


# my_set = {1,2,3,4,5,6,6}
# my_set.add(7)
# print(my_set) # {1, 2, 3, 4, 5, 6, 7}


# my_set = {'a', 1,2,3,4,5,6}
# print(my_set.pop())
# print(my_set)


'''СЛОВАРИ - изменяемая, неупорядоченная, парная.
ключ - неизменяемый тип данных
значение - что угодно пихать
'''

dict

# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# # print(my_dict.get('Key').get(1234).get('key'))
# print(my_dict.get('ONE')) # 1


# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
#
# my_dict[4] = 'FOUR'
#
# print(my_dict) # {'ONE': 1, 2: 'TWO', 3: 'ТРИ', 4: 'FOUR'}



# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# my_dict[4] = 'FOUR'
# print(my_dict.get(4, 'нет такого ключа')) # FOUR

# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# my_dict[2] = 'FOUR'
# print(my_dict.get(4, 'нет такого ключа')) # нет такого ключа


# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# my_dict.setdefault(2, 'Два')
# print(my_dict) # {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}

# setdefault - если такое значение есть, то ничего не происходит. Если нет
# такого значения, то записывает
# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# my_dict.setdefault(4, 'Два')
# print(my_dict) # {'ONE': 1, 2: 'TWO', 3: 'ТРИ', 4: 'Два'}

'''перезатирка новым словарем'''
# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# new_dist = {'ONE': 10, 2: 'Two!', 4: 'Четыре'}
# my_dict.update(new_dist)
# print(my_dict) # {'ONE': 10, 2: 'Two!', 3: 'ТРИ', 4: 'Четыре'}


# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# new_dist = {'ONE': 10, 2: 'Two!', 4: 'Четыре'}
# keys = {'ONE', 2, 3}
# print(my_dict.fromkeys(keys))
# print(my_dict)


# my_dict = {'ONE': 1, 2: 'TWO', 3: 'ТРИ'}
# new_dist = {'ONE': 10, 2: 'Two!', 4: 'Четыре'}
#
# for i in my_dict.keys(): # по ключам .values по значениям, .items по картежам
#     print(i)



# my_dict = {'ONE': 1, '2': 'TWO', '3': 'ТРИ'}
# new_dist = {'ONE': 10, 2: 'Two!', 4: 'Четыре'}
#
# for key, value in my_dict.items():
#     if key.isdigit():
#         print(value)



# my_dict = {'ONE': 1, '2': 'TWO', '3': 'ТРИ'}
# new_dist = {'ONE': 10, 2: 'Two!', 4: 'Четыре'}
#
# my_set = {'123123', 'sdfdf', '123', 123, 'd'}
#
# for item in my_set:
#     print(item)


# массив
# from array import *
#
# my_array = array('i', (1,2,3,4,5,6,7,8,9,0))
# print(my_array[3])

#=========================


# my_list = []
# for i in range(10):
#     my_list.append(i)
#
# print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# или записать коротко

# my_list = [i for i in range(10)]
# print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# random-ЫЕ числа
# my_list = [random.randint(0, 100) for _ in range(10)]
# print(my_list)

# my_list = [i**3 for i in range(10) if not i%2]
# print(my_list)

# создать множество
my_list = {i for i in range(10)}
print(my_list)