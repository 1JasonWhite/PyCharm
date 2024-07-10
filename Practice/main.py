
import random
koloda = list(range(11))
random.shuffle(koloda)
print('Поиграем чувак ? ))')

count = 0

while True:
    choice = input('Будете брать карту? y/n\nВаш ответ -> ')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Извините, но Вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, Вы набрали 21 !')
            break
        else:
            print('У Вас %d очков.' %count)
    elif choice == 'n':
        print('У Вас %d очков и Вы закончили игру.' %count)
        break

