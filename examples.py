# cherry = input('Введите вес черешни(кг): ')
# cherry = float(cherry)
# sum = input('Введите купюру, которую даете кассиру: ')
# sum = int(sum)
# kg = int(38)
# print(int(sum - (cherry * kg)))
# import random

# cena = 2
# ves = 3
# summ = 10
# print(summ - (cena * ves))


# cherry = input(str('Черешня'))
# cena = int(2)
# print(cena)
# kg = int(3)
# print(kg)
# summ = int(10)
# print(summ)
#
# print('Чек')
# print(f'{kg}кг - {cena}руб/кг')
# print(f'Итого: ', kg * cena, 'руб')
# print(f'Внесено: {summ}руб')
# print(f'Сдача: {summ -(kg * cena)}руб')


# a = input("Введи цифру 1 -> ")
# a = int(a)
#
# if 1 <= a <= 1:
#     print('купи слона')
# else:
#     print('Неверно !!!')


# ============================
# import random
# a = random.randint (0,100)
# print(a)
# ============================

# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# print("Введите число: ")
# a = int(input())
# print(f'Вы ввели нахождение {a}!')
#
# factorial = 1
# while a > 1:
#     factorial = factorial * a
#     a = a - 1
#
# print(f'Произведение чисел = {factorial}')


# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 5]

# for i in list_1: # переборка цифр
#     print(i)

# print(len(list_1)) # узнать количество элементов

# print(list_1[0]) # обращение к цифре

# ======================
# добавление цифр
# list_1 = [1, 5]
# print(list_1)
# list_1.append(9)
# print(list_1)
# =======================

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# []
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# ==========================

# Кортежи

# t = ()
#
# print(type(t))
#
# t = (1, 4, 5)
# print(type(t))
#
# v = [1, 4, 6]
# print(v)
# print(type(v))
#
# v = tuple(v)
# print(v)
# print(type(v))

# ===================

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# # colors.remove('red')
# # print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# # colors.discard('red') # ok


#
# list_1 = [1, 1, -1, 3, 4, 4]
#
# list_1.append(9)
# print(list_1)

# import random
# a = random.randint (2, 100)
# print(a)

# for i in list_1: # переборка цифр
#     print(i)

# print(len(list_1)) # узнать количество элементов

# from random import randint
#
# lis = list()
# lens = int(input("Введите длину списка: "))
# for i in range(lens):
#     lis[i] = randint(0, 100)
# print(lis)
# numbers = 0
# for i in range(len(lis)):
#     for j in range(len(lis)):
#         if i == j:
#             numbers += 1
# print(numbers)


# my_list = list()
# number = int(input('Введите длину списка: '))
# for i in range(number):
#     my_list.append(randint(0, 10))
# print(my_list)
#
# find_number = int(input('Введите искомое число: '))
# print(f'Цифра {find_number} встречается: ', my_list.count(find_number),'раз(а)')


# ====== урок 7

#map

# my_list = list(map(int, list('123456789')))
#
# def even(num: int):
#     if num % 2 == 0:
#         return True
#     return False
#
# even_list = list(filter(even, my_list))

# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i])

# print(even_list)



# a = lambda x, y: x + y
# print(a(1, 2))

# my_list = [str(x) for x in range(10) if x % 2 == 0]
# print(my_list)

# ================================================================
# взято с лекции №4 pdf file
# def f(x):
#     return x ** y
# x = int(input('Введите число: '))
# y = int(input('Введите степень: '))
# g = f
# print(f'f(x) = ', f(x))
# print(f'g(x) = ', g(x))


# def calc(x):
#     return x + 10
# print(calc(10))


# def sum(x, y):
#     return x + y
#
# def mylt(x, y):
#     return x * y
#
# print(sum(4, 5))
# print(mylt(4, 5))


# def calc(x, y):
#     return x * y
# def math(op, a, b):
#     print(op(a, b))
#
# math(lambda x,y: x + y, 5, 45)


# list = [1, 2, 3, 4, 5, 8, 15, 23, 38]
# out = []
# print(list)
# for i in list:
#     if i % 2 == 0:
#         print(i)
#         out.append((i, i ** 2))
# print(out)

# from random import randint
#
# list = []
# out = []
# for i in range(10):
#     list.append(randint(0, 99))
# print(list)
# for i in list:
#     if i % 2 == 0:
#         print(i)
#         out.append((i, i ** 2))
# print(out)


# phrase = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# print(phrase)
#
# for i in range(len(phrase)):
#     if phrase[i] == 'а':
#         print('парам пам-пам')


phrase_1 = input('Введите фразу: ')
phrase_2 = 'пара-ра-рам рам-пам-папам па-ра-па-да'
if phrase_1 == phrase_2:
    print('Парам пам-пам')
else:
    print('Пам парам')










