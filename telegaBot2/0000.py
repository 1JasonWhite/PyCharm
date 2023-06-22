'''
number = int(input('Введи 4х значное число: '))
if number > 9999:
    exit(print('Вы ввели больше 4х цифр !!!'))
a = number % 10
b = number % 100 // 10
c = number // 100 % 10
d = number // 1000
print(a,b,c,d)



# Калькулятор
a = int(input('Введи число: '))
b = int(input('Введи второе число: '))

print('Что нужно сделать?')
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

if choice == '1':
    print(a+b)
elif choice == '2':
    print(a-b)
elif choice == '3':
    print(a*b)
elif choice == '4':
    print(a/b)


bank = int(input('Введите число: '))
if bank >= 75000:
    print('Курс приобретен!')
else:
    print('Накопи еще чуток')



apples = 41
boxes = 3
f_boxes = 41 / 3
print(f_boxes)
ost_apples = 41 % 3
print(ost_apples)



num = int(input('Введи 3х значное число: '))
num_house = num % 10
print('Номер дома: ', num_house)
num_apart = num // 10
print('Номер квартиры: ', num_apart)
num_floor = num // 100
print('Этаж: ', num_floor)




bank = int(input('Введите состояние счета: '))
if bank >= 75000:
    bank -= 75000
    print('Курс приобретен!')
else:
    print('Не хватает денег! Пополните счет!')
print('Удачи!')
print('Остаток на счете: ', bank)


#################################################################

# Задача 1. Датчик погоды
rain = int(input('На улице идёт дождь?'))
if rain == 1:
    print('Пошёл дождь. Возьмите зонтик!')
elif rain == 0:
    print('Дождя нет!')
else:
    print('Ввели не те цифры !!! Еще раз попробуй')




# Задача 2. Поступление
rus_lang = int(input('Введите количество баллов по русскому языку: '))
math = int(input('Введите количество баллов по математике: '))
informatics = int(input('Введите количество баллов по информатике: '))
passing_grade = rus_lang + math + informatics
if passing_grade >= 270:
    print('\nВы набрали балов: ', passing_grade)
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('\nВы набрали балов: ', passing_grade)
    print('К сожалению, ты не прошёл на бюджет.')




# Задача 3. Следим за расписанием
num = int(input('Введите число: '))
if num % 2 == 0:
    print('Четное число!')
else:
    print('Нечетное число!')


# Задача 4. Калькулятор скидки
product_1 = int(input('Цена 1-го продукта: '))
product_2 = int(input('Цена 2-го продукта: '))
product_3 = int(input('Цена 3-го продукта: '))
sum_products = product_1 + product_2 + product_3
discount = 0
if sum_products >= 10000:
    discount = sum_products * 10 / 100
    print('Сумма без скидки: ', sum_products,'руб')
    print('Скидка 10%: ', discount,'руб')
    print('К оплате: ', sum_products - discount,'руб')



#Задача 5. Модуль числа
a = int(input('Введите число: '))
print('Ввел: ', a)
if a < 0:
    a = -a
    print('Ответ: ', a)
elif a > 0:
    print('Ответ: ', a)


# Задача 6. Игра в кубики
num_1 = int(input('Кубик Кости: '))
num_2 = int(input('Кубик владельца: '))
difference = num_1 - num_2
sum = num_1 + num_2
if num_1 >= num_2:
    print('Разность: ',difference)
    print('Игрок платит')
else:
    print('Сумма: ',sum)
    print('Владелец платит')
print('Игра окончена!')



# Задача 7. Хватит ли зарплаты

hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите траты на еду: '))
salary = ((200 * hours) / 2**3) + hours
credit_food = credit + food

if salary >= credit_food:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать больше!')
print('Зарплата:', salary)


#Задача 8. Максимальное число (по желанию)
first_num = int(input('Первое 3х значное число: '))
second_num = int(input('Второе 3х значное число: '))
third_num = int(input('Третье 3х значное число: '))

f_a = first_num % 1000 // 100
f_b = first_num % 100 // 10
f_c = first_num % 10
sum_1 = f_a + f_b + f_c

s_a = second_num % 1000 // 100
s_b = second_num % 100 // 10
s_c = second_num % 10
sum_2 = s_a + s_b + s_c

t_a = third_num % 1000 // 100
t_b = third_num % 100 // 10
t_c = third_num % 10
sum_3 = t_a + t_b + t_c

if sum_1 > sum_2:
    print('Сумма первого 3х значного числа:', sum_1)
elif sum_2 > sum_3:
    print('Сумма второго 3х значного числа:', sum_2)
else:
    print('Сумма третьего 3х значного числа:', sum_3)

'''










