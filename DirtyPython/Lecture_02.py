# list_contcacts = []

# print(bool(number))

# if number.isdigit():
#     print('Зашли в тело IF, тут цифры(а)')


# print(0 < int (number) < 11)
# if list_contcacts:
#     print(list_contcacts)
# # if 0 == 0:
# elif not list_contcacts:
#     print('Здесь выполнено ELIF')
# else:
#     print('Список пуст')



# ball = input(str('Какого цвета мяч? '))
#
# if ball == 'RED':
#     print('Мяч красный')
# elif ball == 'BLUE':
#     print('Мяч синий')
# elif ball == 'YELLOW':
#     print('Мяч желтый')
# else:
#     print('не знаю цвета')

# and 1 * 1 1
# 1 * 0 0
# 0 * 0 0
# 0 * 0 0
#
# or
# 1 + 1 2
# 1 + 0 1
# 0 + 1 1
# 0 + 0 0

# length = int(input('Введите длину: '))
# width = int(input('Введите ширину: '))
# count = int(input('Введите количество кусочков: '))
#
# if length * width > count and (count % length == 0 or count % width == 0):
#     print('Yes')
# else:
#     print('No')

# i = 0
#
# while 0 < 10:
#     print('Ура')
#     if i == 10:
#         break
#     i += 1


# i = 0
# while True:
#     number = input('Введите число: ')
#     if number == '':
#         break



# i = 0
# number = 'dfwfwf'
# while True:
#     number = input('Введите число: ')
#     if number.isdigit():
#         continue # цикл будет повторяться снова (pass - пропускает)
#     print('Это не число')


# i = 0
# while i < 10:
#     print('Ура')
#     i = i + 1
# else:
#     print('цикл дожил до конца')



# i = 0
# while i < 10:
#     if i == 7:
#         break
#     print('Ура')
#     i = i + 1
# else:
#     print('цикл дожил до конца')



# СПИСКИ

my_list = []

for i in range(5):
    my_list.append(i)
print(my_list)



# my_list = []
#
# for i in range(10):
#     my_list.insert(0, i)
#     print(my_list)

''' range - позволяет создать последовательность, создание чего нибудь
перебираемого
range(start:finish:step)
'''


# my_list = ['1', 2, 'Три', 'IV']
#
# for index in range(len(my_list)):
#     print(index)



# my_list = ['1', 2, 'Три', 'IV']
# print(my_list)
#
# my_list[3] = 'ЧЕТЫРЕ'
# print(my_list)
# for index in range(len(my_list)):
#     my_list[index] = 3
# print(my_list)


# my_list = ['1', 2, 'Три', 'IV']
# print(my_list)
#
# for index in my_list:
#     print(index)
# else:
#     print('Умерло своей смертью')
# print(my_list)



# for index in 'jkdbwjvlwnvkwlnwuhdghc;igqmg;cqhgxq':
#     if index == 'w':
#         print('Попалась сучка!')
#         break
#     print(index)



# trigger = True
# count = 0
# for index in 'jkdbjvlnvkwlnuhdgwhc;igqwmg;cqhgxq':
#     if index == 'w':
#         count += 1
#         print(f'Попалась сучка! уже {count} раз')
#         trigger = False
# if trigger:
#     print('К сожалению w нет в этом слове')


# count = 0
# for i in 'jkdbjvlnvkwlnu':
#     for k in range(10):
#         for m in ['!', '?']:
#             print(i, k, m)
#             count += 1
# print(f'{14*20} = {count}')



# number = int(input('Введите от 1 - 4 !!! '))
#
# if number == 1:
#     print('Один')
# elif number == 2:
#     print('Два')
# elif number == 3:
#     print('Три')
# elif number == 4:
#     print('Четыре')
# else:
#     print('Больше не могу')


# days_ofweek = int(input('Введите номер дня недели: '))
#
# if days_ofweek == 1:
#     print('Понеделиник')
# elif days_ofweek == 2:
#     print('Вторник')
# elif days_ofweek == 3:
#     print('Среда')
# elif days_ofweek == 4:
#     print('Четверг')
# elif days_ofweek == 5:
#     print('Пятница')
# elif days_ofweek == 6:
#     print('Суббота')
# elif days_ofweek == 7:
#     print('Воскресенье')


# match number:
#     case 1:
#         print('Один')
#     case 2:
#         print('Два')
#     case 3:
#         print('Три')
#     case 4:
#         print('Четыре')

