'''
Задача №39. Решение в группах
Даны два списка чисел. Требуется вывести те элементы
первого списка (в том порядке, в каком они идут в первом
массиве), которых нет во втором списке. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы списка. Затем число M - количество
элементов во втором списке. Затем элементы второго списка
Ввод:                       Вывод:
7                           3 3 2 12

3 1 3 4 2 4 12

6
4 15 43 1 15 1
'''

from random import randint

list_1 = list()
lens = int(input("Введите длину 1-го списка: "))
for i in range(lens):
    list_1.append(randint(0, 10))

list_2 = list()
lens = int(input("Введите длину 2-го списка: "))
for i in range(lens):
    list_2.append(randint(0, 10))

print(list_1)
print(list_2)

list_3 = list_1 + list_2
print(list_3)
