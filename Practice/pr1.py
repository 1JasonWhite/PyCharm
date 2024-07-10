from decimal import Decimal

# #
# # num = Decimal('5.56')
# # print(num*10)
#
# # string = 'еще одно слово'
# # string_slice = string[4:8] # от 4 индекса включительно по 8 не включительно
# # string_slice2 = string[:4:2] # [:4:2] двойка обозначает шаг
# # string_slice3 = string[::-1] # переворачивает строку задом на перед
# # print(string)
# # print(string_slice)
# # print(string_slice2)
# # print(string_slice3)
#
# string = 'Ахуенный       питон       мля !!!'
# print(string[::-1])
# print(string.find('й')) # нахождение индекса по букве
# print(string.split(' ')) # разбивает строку на список по пробелам
# print(string.replace(' ','-', 4)) # Заменяет одну букву(символ) на другую(й), а цифра 4 заменяет первые
#                                   # четыре символа (Ахуенный----   питон       мля !!!)
#
# num = '324'
# print(num.isdigit()) # True проверяет, является ли введенное числом
# print(string.count('н')) # сколько раз встречается в тексте симпол или слово
# print(string[0:10].strip()) # отсекает все символы ТОЛЬКО с краёв выделенного слова
#
# result = ()
#
# if result:
#     print('Все ок')
# else:
#     result = (5,6,7)
#     print(result)
# number = (0.1 + 0.1 + 0.1 - 0.3)
#
# num = Decimal(number)
# if num:
#     print(100 / num)
# while True:
#     number = input("Введите число: ")
#
#     if number.isdigit() and 0 < int(number) < 10:
#         print('Вы ввели число от 1 - 9')


number = int(input('Введите число: '))

number = 'четное' if number%2 == 0 else 'нечетное'
print(number)
