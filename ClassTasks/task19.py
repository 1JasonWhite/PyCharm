# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint
lis = list()
lens = int(input("Введите длину списка: "))
for i in range(lens):
    lis.append(randint(0, 10))
print(lis)
k = int(input("Введите длину отступа: "))
for i in range(k):
    lis.insert(0, lis.pop())
print(lis)