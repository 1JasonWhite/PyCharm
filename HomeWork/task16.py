'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''


from random import randint

my_list = list()
length_list = int(input('Введите длину списка: '))
for i in range(length_list):
    my_list.append(randint(0, 10))
print(my_list)

find_number = int(input('Введите искомое число: '))
print(f'Цифра {find_number} встречается: ', my_list.count(find_number),'раз(а)')