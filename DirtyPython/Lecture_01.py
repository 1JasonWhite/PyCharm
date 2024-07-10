# var = int(input('Введите переменную'))
# print(var, end=", ") # вывод в одну строку
# print(var, end=", ")

# =============

# int - неизменяемый тип данных
# float - неизменяемый тип данных
# str - неизменяемый тип данных
# bool - сравнения

# int
# var_1 = 1
# var_2 = '1'
# var_3 = 0.1
# var_4 = True
#
# print(type(var_1))
# print(type(var_2))
# print(type(var_3))
# print(type(var_4))

# number_1 = 10
# number_2 = 5
#
# print(number_1 + number_2)
# print(number_1 - number_2)
# print(number_1 / number_2)
# print(number_1 * number_2)
# print(number_1 // number_2)
# print(number_1 % number_2)
# print(number_1 ** number_2)
# print(number_1 == number_2)

# a = 5
# b = a
# print(a)
# print(b)
# a = a + 1
# print(a)
# print(b)

#============

# float
# print(0.1 + 0.1 + 0.1 - 0.3)
#
# #=====
#
# a = 0.1 + 0.1 + 0.1 - 0.3
# b = 0
# print(a == b)
#
# #=====
#
# a = 0.56
# print(a)
# print(a * 100)

#=====

# from decimal import Decimal
# a = Decimal('0.56')
# print(a)
# print(a * 100)

#=====

# str

# text = 'wdwf we rwerer3423er wer324234 wfwefwwe'
#
# print(text)
# print(text.split(' ')) # распиливает по пробелам
# print(text.replace(' ', '***')) # замена символа на другой(пробел на ***)

'''text = '1231'
print(text)
print(text.isdigit()) # вытащить цифры(работа с цифрами)
'''
# print(text.isalpha())
# print(text.lower()) # переводит к нижнему регистру
# print(text.upper()) # переводит к верхнему регистру
# print(text.index('e')) # выдает букву по индексу
# print(text.find('e'))
# print(text.count('3')) # подсчитывает сколько раз встречается буква

# print(f'Исходный текст = {text}')

#=====
# срезы
# text = 'wdwf we rwerer3423er wer324234 wfwefwwe'
# print(text)
# print(text[5:-8]) # print(text[start:finish:step])
# print(text.[text.index('w'):text.rindex('e')])

# bool
# >
# <
# =>
# <=
# ==
# !=
# not
# or
# and

# a = True
# b = False
# print(a)
# print(a and b)

