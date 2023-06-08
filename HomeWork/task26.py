'''
Задача 26:  Напишите программу, которая на вход принимает два
числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''



# number_1 = int(input('Введите 1-е число: '))
# number_2 = int(input('Введите 2-е число: '))
# print(f'Ответ будет таков: {number_1**number_2}')


def power(number_1, degree):
    if degree == 0:
        return 1
    elif degree % 2 == 0: # проверяем на четность
        return power(number_1, degree//2) * power(number_1, degree//2)
    else:
        return number_1 * power(number_1, degree//2) * power(number_1, degree//2)

number_1 = int(input("Введите число: "))
degree = int(input("Введите его степень: "))

print(f'{number_1} * {degree} = {power(number_1, degree)}')
# result = power(number_1, degree)
# print(result)





