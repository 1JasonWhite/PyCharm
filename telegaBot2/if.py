'''
cars = ['toyota','subaru','bmw','suzuki']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

'''

'''
number_1 = int(input("Ввeдите число 5: "))
if number_1 == 5:
    print(f'Вы ввели: ',number_1)
else:
    print('Вы ввели неправильное число!!!')
    exit()
number_2 = int(input("Ввeдите число 6: "))
if number_2 == 6:
    print(f'Вы ввели: ', number_2)
else:
    print('Вы ввели неправильное число!!!')
    exit()
answer = number_1 + number_2
if answer == 11:
    print("Это правильный ответ!!!")
else:
    print("Это неправильный ответ!!! Должно получиться 11")
'''

'''
number_1 = int(input("Ввeдите число 5: "))
if number_1 !=5:
    print('Вы ввели неправильное число!!!')
    exit()
else:
    print(f'Вы ввели: ',number_1)

number_2 = int(input("Ввeдите число 5: "))
if number_1 !=6:
    print('Вы ввели неправильное число!!!')
    exit()
else:
    print(f'Вы ввели: ',number_2)
answer = number_1 + number_2
if answer == 11:
    print("Это правильный ответ!!!")
else:
    print("Это неправильный ответ!!! Должно получиться 11")
'''

# Поиск слов в списке
'''
list = ['mashrooms','meat','milk','juce']
if input("Введите для поиска: ") in list:
    print("В списке")
else:
    print("НЕТ в списке")
'''

'''
banned_users = ['Andry','Jack','Nick','Josh']
user = input("Write the name: ")

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", you can't post")
'''
'''
age = int(input("Write your age: "))
if age < 4:
    print("Вам вход бесплатный")
elif age < 18:
    print("Детям от 4 до 18 - 100руб")
elif age < 25:
    print("Взрослый билет - 150руб")
elif age < 50:
    print("Пенсионерам бесплатно !")
'''

# ИЛИ
'''
age = int(input("Ваш возраст: "))
if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 25:
    price = 15
print("Твоя плата составляет $" + str(price) + ".")
'''

'''
age = int(input("Твой возраст: "))
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
'''
'''
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
'''

'''
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
'''

'''
alien_color = ['green','yellow','red']
if input('Напишите цвет: ') in alien_color:
    print('Да, этот цвет есть, вы заработали 5 очков')
else:
    print('Этого цвета нет!')
'''

'''
alien_color = []
alien_color.append(input("Введите в список цвет 1: "))
alien_color.append(input("Введите в список цвет 2: "))
alien_color.append(input("Введите в список цвет 3: "))
print(alien_color)
if input('Напишите цвет: ') in alien_color:
    print('Да, этот цвет есть, вы заработали 5 очков')
else:
    print('Этого цвета нет!')
'''

'''
age = int(input("Введите возраст: "))
if age < 2:
    print("Вы еще младенец")
elif age < 10:
    print("Вы еще ребенок")
else:
    print("Ты уже взрослый")
'''

"""
userInput = int(input('Enter your age: '))
print(type(userInput))
if userInput < 2:
    print("младенец")
elif userInput < 4:
    print ("малыш")
elif userInput < 13:
    print ("ребенок")
elif userInput < 20:
    print("подросток")
elif userInput < 65:
    print("взрослый")
elif userInput >= 65:
    print("пожилой человек")
"""


"""
additives = []
additives.append(input("write toppings: "))
additives.append(input("write toppings: "))
additives.append(input("write toppings: "))
additives.append(input("write toppings: "))
print(additives)
for additivess in additives:
    if additivess == "зеленый лук":
        print("Зеленого лука нет")
    else:
        print("Было добавленно" + additivess + ".")
"""
"""
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
     print("Are you sure you want a plain pizza?")
"""

"""
available_toppings = []
available_toppings.append(input('Добавьте в меню ингр-ты 1: '))
available_toppings.append(input('Добавьте в меню ингр-ты 2: '))
available_toppings.append(input('Добавьте в меню ингр-ты 3: '))
available_toppings.append(input('Добавьте в меню ингр-ты 4: '))
print("Ваше составленное меню: ", available_toppings)

print("Сделайте ваш заказ!")

requested_toppings = []
requested_toppings.append(input("1 Добавьте в ваше блюдо из меню: "))
requested_toppings.append(input("2 Добавьте в ваше блюдо из меню: "))
requested_toppings.append(input("3 Добавьте в ваше блюдо из меню: "))
requested_toppings.append(input("4 Добавьте в ваше блюдо из меню: "))
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Добавлено " + requested_topping + '.')
    else:
        print('Извините, у нас нет' + requested_topping + '.')
"""
"""
name = []
name.append(input("Добавьте имена в список -> "))
name.append(input("Добавьте имена в список -> "))
name.append(input("Добавьте имена в список -> "))
name.append(input("Добавьте имена в список -> "))
for names in name:
    if names == 'admin':
        print('Привет админ !')
    else:
        print('Привет пользователь, ',names)
"""
"""
num = []
print('Напишите цифры от 1 - 9 ->')
num.append(input('первая: '))
num.append(input('вторая: '))
num.append(input('третья: '))
num.append(input('четвертая: '))
num.append(input('пятая: '))
num.append(input('шестая: '))
num.append(input('седьмая: '))
num.append(input('восьмая: '))
num.append(input('девятая: '))
print(num)
for nums in num:
    if nums == '1':
        print("1st")
    if nums == '2':
        print("2nd")
    if nums == '3':
        print("3rd")
    if nums == '4':
        print("4th")
    if nums == '5':
        print("5th")
    if nums == '6':
        print("6th")
    if nums == '7':
        print("7th")
    if nums == '8':
        print("8th")
    if nums == '9':
        print("9th")

"""

"""
num1 = float(input("Введите 1 число: "))
num2 = float(input("Введите 2 число: "))

if num2 > num1:
    print(num2, "Большее число")
    print(num1, "Меньшее число")
if num1 > num2:
    print(num1, "Большее число")
    print(num2, "Меньшее число")

"""


num1 = int(input("Введите число: "))
if num1 % 2 == 0:
    print(f"{num1} - Число четное!")
else:
    print(f"{num1} - Число нечетное!")






#стр 96