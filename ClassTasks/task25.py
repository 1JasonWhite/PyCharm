'''
Задача №25.
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2в добавляется к символам с помощью постфикса формата _n.
'''
import random

my_list = [random.randint(0,10) for _ in range(20)]
print(my_list)

counter = {}

for x in my_list:
    counter[x] = counter.get(x, 0) + 1
    if counter.get(x) < 2:
        print(x, end='')
    else:
        print(str(x) + '_' + str(counter.get(x) - 1), end=' ')



