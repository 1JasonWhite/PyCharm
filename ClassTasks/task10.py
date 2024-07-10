# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint

num = int(input('Введите цифру: '))

for i in range(num):
    print(randint(0, 1))

# a = (1, 0, 1, 1, 0, 0)
#
# for element in a:
#     if element == 0:
#         print(element)

# line=input("").split()
# cnt=0
# for i,s in enumerate(line):
#     if s.isdigit():
#         cnt+= len(s) # считаем цифры
# if cnt == 0:
#     print("числа не обнаружены")
# else:
#     print("",cnt)



