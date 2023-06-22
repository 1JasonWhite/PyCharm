'''
man = {'name': 'Pavel','2nd name': 'Kravchenko',
       'age': 37,'maried': 'yes','cat': 'Lisa'}
print(man['name'])
print(man['cat'])
print(man['2nd name'])
print(man['maried'])
print(man['age'])

######

alien = {}
alien[input('Введите ключ: ')] = input('Введите значение: ')
alien[input('Введите ключ2: ')] = input('Введите значение2: ')
alien[input('Введите ключ3: ')] = input('Введите значение3: ')
alien[input('Введите ключ4: ')] = input('Введите значение4: ')
print(alien)
print(alien['имя'])
print(alien['кот'])
print(alien['жена'])
print(alien['количество в семье'])

#######
# Замена ключ-значение

man = {'color': 'blue'}
print(f'Man is ', man['color'])

man['color'] = 'black'
print(f'Man is ',man['color'])

#######

alien_0 = {'x_position': int(input('Задать позицию x: ')),
           'y_position': int(input("Задать позицию y: ")),
           'speed': input('Задать скорость: ')}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
# Пришелец двигается быстро.
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))



# Удаление ключ-значение

man = {'hands': 4, 'head': 1}
print(man)

del man['head']
print(man)


f_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print('Sarah is f_lang is '+ f_lang['sarah'].title() + '.')


man = {'Имя': input('Введите имя: '), 'Фамилия': input('Введите фамилию: '),
       'Возраст': int(input('Введите возраст: ')),
       'Город': input('Название вашего города: ')}

print(man['Имя'])
print(man['Фамилия'])
print(man['Возраст'])
print(man['Город'])

print(man)

del man[input('Введите для удаления: ')]
print(man)



#Перебор всех пар «ключ—значение»

user = {'name': 'Pavel',
        'last': 'Kravchenko',
        'age': '37'}

for key, value in user.items():
    print("\nKey: " + key)
    print("Value: " + value)



user = {'Pavel': 'Python',
        'Olya': 'C',
        'Lisa': 'Java'}

for name, lang in user.items():
    print(f"{name}'s favorite language is ", lang)



user = {'Pavel': 'Python',
        'Olya': 'C',
        'Lisa': 'Java'}

for name in user:
    print(name)



fav_lang = {'Pavel': 'Python',
        'Olya': 'C',
        'Lisa': 'Java'}

friends = ['Olya','Pavel','Lisa']
for name in fav_lang:
    print(name)

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
        fav_lang[name].title() + "!")
'''


f_lang = {input('Впиши имя 1: '): 'Python',
        input('Впиши имя 2: '): 'C',
        input('Впиши имя 3: '): 'Java'}
if 'Виталя' not in f_lang:
    print('Виталя не участвовал')
if 'Мама' not in f_lang:
    print('Mama не участвовала')
if 'Павел' not in f_lang:
    print('Павел не участвовал')
if 'Оля' not in f_lang:
    print('Оля не участвовала')
if 'Лиза' not in f_lang:
    print('Лиза не участвовала')
if 'Папа' not in f_lang:
    print('Папа не участвовал')



