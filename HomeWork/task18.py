'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''

from random import randint

my_list = list()
length_list = int(input('Введите длину списка: '))
close_element = int(input('Введите заданное число Х: '))
for i in range(length_list):
    my_list.append(randint(0, 10))

min_dist = float('inf')
nearest = my_list[0]
for item in my_list:
    if abs(close_element - item) < min_dist:
        min_dist = abs(close_element - item)
        nearest = item

if (min_dist + close_element) in my_list:
    nearest.append(min_dist + close_element)
elif (close_element - min_dist) in my_list:
    nearest.append(close_element - min_dist)
print(f'Ближайшее число к {close_element} будет {nearest}')

print(my_list)

# НЕ ПОНИМАЮ, ЧТО ДОЛЖЕН ПИСАТЬ ДАЛЬШЕ

