
'''
age = 37
message = "C " + str(age) + "-милетием!"
print(message)

print(4*2)
print(5+3)
print(10-2)
print(16//2)

#созданиме списка и замена элемента
names = ['Grigori','Pavel','Olga']
print(names)
print(names[0])
names[0] = 'Ludka'
print(names)
print(names[0])
names.append('Vitaliy')
print(names)

#создание пустого списка + добавление по-одному элементу
motorcycles = []
print(f'list ->',motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('suzuki')
print(motorcycles)
motorcycles[0] = 'toyota'
print(motorcycles)

#Добавление элемента
print(f'было -> ', motorcycles)
motorcycles.insert(1, 'nissan')
print(f'стало -> ',motorcycles)

#Удаление элемента
print(f'было -> ', motorcycles)
del motorcycles[0]
print(f'стало -> ',motorcycles)

cars = ['toyota','honda','nissan']
print(cars)

poppend_cars = cars.pop(1)
print(cars)
print(poppend_cars)

cars = ['toyota','honda','nissan']
print(cars)
cars.remove('honda')
print(cars)


cars = ['toyota','honda','nissan']
print(cars)
too_expensive = 'honda'
cars.remove(too_expensive)
print(cars)
print("\nA " + too_expensive.title() + " is too expensive for me.")


#Задача
list = ['Pavel','Olga','Lisa']
print(f'Люди, которых еще не пригласили ->',list)

first_invited = list.pop()
print(f'Люди, которые еще не были приглашены', list)
print(f'Люди, которых пригласили: ', first_invited)
second_invited = list.pop()
print(f'Люди, которые еще не были приглашены', list)
print(f'Люди, которых пригласили: ', second_invited)
print(list)

#Сортировка
cars = ['mercedes','audi','bmw','toyota','suzuki','jac']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)

cars = ['mercedes', 'audi', 'bmw', 'toyota', 'suzuki', 'jac']
print(f'Количество машин в списке: ', len(cars))
print(cars[5])
print(len(cars))

#Цикл for
names = ['pavel','olga','vitaliy','luda','ura','galya','vladimir']
names.sort()
for name in names:
    print(name.title() + ', член нашей семьи!')
print('\n''Спасибо, это весь список!')


pizzas = ['peperoni','threecheez','mashrooms']
for pizza in pizzas:
    print(pizza + ' , все равно люблю другую пиццу')
print('Да похер, любую пиццу люблю')


for value in range(1,5):
    print(value)

numbers = list(range(1,11))
print(numbers)


#Использование range() для создания числового списка
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    #squares.append(value**2)
print(squares)

for value in range(1,31):
   if value % 3 == 0:
    print(value, end=" ")

dig = [2,5,7,9,3,1,8]
print(dig)
dig.sort()
print(dig)
print("max: ", max(dig))
print("min: ", min(dig))
print("sum: ", sum(dig))

players = ['pavel','olga','vit','luda','ura','volodya','galya']
print(players[1:3])
'''


#Копирование списка

'''
my_foods = ['pizza','soup','apples','mango','pasta']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)


                       # кортежи
corp = (12,1,4,5,93)
for corp in corp:
    if corp > 10:
        print(corp, end=' ')

dim = (100,50)
print('original dim')
for dim in dim:
    print(dim, end=' ')

dim = (300,100)
print('\nmodif dim')
for dim in dim:
    print(dim, end=' ')
'''


menu = ('pizza','soup','pasta','tea')
print(type(menu))
for menu in menu:
    print(menu, end=', ')

menu = ('pizza','soup','coffe','tea')
print('\nМеню ресторана: ')
for menu2 in menu:
    print(menu2,end=', ')






