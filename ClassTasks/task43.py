'''
Задача №43.
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
'''

from random import randint

minimal = int(input('Write the minimal number: '))
maximal = int(input('Write the maximal number: '))
print(my_list := [randint(minimal, maximal) for _ in range(20)])
kol = 0
for i in set(my_list):
    kol += my_list.count(1) // 2
print(kol)